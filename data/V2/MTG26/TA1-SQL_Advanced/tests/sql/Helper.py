import os
from sql import BaseAccess as Ba

try:
    import sqlparse
except ImportError:
    print("Trying to Install required module: sqlparse\n")
    os.system('pip install sqlparse')
    import sqlparse

try:
    import requests
except ImportError:
    print("Trying to Install required module: requests\n")
    os.system('pip install requests')
    import requests

from sqlparse.sql import Identifier, IdentifierList, Where, Comparison, Function, Parenthesis
from sqlparse.tokens import Keyword, DML, Name

def normalizeSQLQuery(query, baseDict):
    try:
        query = query.replace("\"", "'")
        parsed = sqlparse.parse(query)[0]
        parsed.tokens = [token for token in parsed.tokens if not token.is_whitespace]
    except Exception as e:
        raise Exception(f"\nSyntax-Fehler in der SQL-Abfrage.")

    formatted_query = []
    alias_map = {}

    def process_identifier(identifier, alias_map, baseDict: dict):
        if isinstance(identifier, Identifier):
            if identifier.get_real_name() and identifier.get_parent_name():
                return f"{alias_map[identifier.get_parent_name()]}.{identifier.get_real_name()}"
            elif identifier.get_real_name():
                tables = findTableForColumn(baseDict, identifier.get_real_name(), alias_map.keys())
                if len(tables) == 1:
                    return f"{tables[0]}.{identifier.get_real_name()}"
                else:
                    return f"{identifier.get_real_name()}"
        return str(identifier)

    def process_select(select, alias_map):
        select_tokens = []
        for token in select.tokens:
            if isinstance(token, IdentifierList):
                for identifier in token.get_identifiers():
                    select_tokens.append(f"{process_identifier(identifier, alias_map)} as {identifier.get_real_name()}")
            elif isinstance(token, Identifier):
                select_tokens.append(f"{process_identifier(token, alias_map,  baseDict)} as {token.get_real_name()}")
            else:
            #elif token.is_whitespace:
                continue
            #else:
            #    select_tokens.append(str(token))
        select_tokens.sort()
        return ",".join(select_tokens)

    def process_from(from_, alias_map):
        from_tokens = []
        if hasattr(from_, 'tokens'):
            for token in from_.tokens:
                if isinstance(token, IdentifierList):
                    for identifier in token.get_identifiers():
                        alias_map[identifier.get_real_name()] = identifier.get_alias() or identifier.get_real_name()
                        from_tokens.append(f"{identifier.get_real_name()} {alias_map[identifier.get_real_name()]}")
                elif isinstance(token, Identifier):
                    alias_map[token.get_real_name()] = token.get_alias() or token.get_real_name()
                    from_tokens.append(f"{token.get_real_name()} {alias_map[token.get_real_name()]}")
                #elif token.is_whitespace:
                #    continue
                else:
                    continue
                    #from_tokens.append(str(token))
        from_tokens.sort()
        return ",".join(from_tokens)

    def process_where(where, alias_map, baseDict):
        where_tokens = []
        for token in where.tokens:

            if isinstance(token, Comparison):
                left, operator, right = [t for t in token.tokens if not t.is_whitespace]
                left = process_identifier(left, alias_map, baseDict)
                right = process_identifier(right, alias_map, baseDict)
                if left >= right:
                    left, right = right, left
                    if(operator.value == ">"):
                        operator = "<"
                    elif(operator.value == "<"):
                        operator = ">"

                where_tokens.append(f"{left} {operator} {right}")
            elif token.is_whitespace or token.ttype is Keyword and token.value.upper() == "WHERE":
                continue
            else:
                where_tokens.append(str(token))
        return " ".join(where_tokens)

    # First pass to process FROM clause and populate alias_map
    for token in parsed.tokens:
        if token.is_whitespace:
            continue
        elif token.ttype is Keyword and token.value.upper() == 'FROM':
            formatted_query.append('FROM')
            pass
        elif isinstance(token, IdentifierList) and formatted_query and formatted_query[-1] == 'FROM':
            formatted_query.append(process_from(token, alias_map))
            process_from(token, alias_map)

    formatted_query = []

    # Second pass to process SELECT and WHERE clauses
    for token in parsed.tokens:
        if token.is_whitespace:
            continue
        elif token.ttype is DML and token.value.upper() == 'SELECT':
            formatted_query.append('SELECT')
        elif token.ttype is Keyword and token.value.upper() == 'FROM':
            formatted_query.append('FROM')
        elif isinstance(token, IdentifierList) and formatted_query and formatted_query[-1] == 'FROM':
            formatted_query.append(process_from(token, alias_map))
        elif isinstance(token, Where):
            formatted_query.append('WHERE')
            formatted_query.append(process_where(token, alias_map, baseDict))
        elif formatted_query and formatted_query[-1] == 'SELECT' and isinstance(token, IdentifierList):
            formatted_query.append(process_select(token, alias_map))
        else:
            formatted_query.append(str(token))

    return " ".join(formatted_query)


def findTableForColumn(data_dict, target_value, relevantTables):
    l = []
    for key, value_list in data_dict.items():
        if key in relevantTables:
            for sublist in value_list:
                if sublist and sublist[0] == target_value:
                    l.append(key)
    return l


def getTableScheme(table_name: str, tableDict: dict):

    tab = tableDict[table_name]

    # Format the schema
    schema = "(" + ",".join([f"{col[0]}:{col[1]}" for col in tab]) + ")"

    #print(schema)
    #schema = "(" +( ",".join([f"{col[1]}:{col[2].upper()}" for col in columns])) +")"
    return schema


def buildAndSendCosetteRequest(baseDict, sql, sol):

    err = ""
    for i in range(2):
        try:
            apiKey="69f7ead93f81da018217bfc1e7b8b56a"

            schema = ""
            for tab in baseDict.keys():
                schema += f"schema sch{tab}{getTableScheme(tab, baseDict)};\n"
            for tab in baseDict.keys():
                schema += f"table {tab}(sch{tab});\n"

            q1 = "query q1\n`"+sql+"`;\n"
            q2 = "query q2\n`"+sol+"`;\n"

            cosette = "-- random Kommentar\n" + schema + q1 + q2 + "verify q1 q2;\n"
            print(cosette)

            r = requests.post("https://demo.cosette.cs.washington.edu/solve",data={"api_key": apiKey, "query": cosette}, verify=False)

            print(r.text)
            return (r.json()['result'],r.text)
            #return r.json()['result']

        except Exception as e:
            err = str(e)
    return ("ERR", err)


def checkEquality(sqlPath, solPath):
    bd = Ba.getTableDict()
    sql = normalizeSQLQuery(Ba.getSQLFromFile(sqlPath), bd)
    sol = normalizeSQLQuery(Ba.getSQLFromFile(solPath), bd)
    if(sql=='' or sol==''):
        return "\n\nSQL-Datei ist leer. Aufgabe wurde noch nicht bearbeitet."
    result = buildAndSendCosetteRequest(bd, sql, sol)

    if(result[0] == "ERR"):
        return "\n\nFehler bei der Überprüfung deiner Abgabe. Es kann keine Aussage über die Korrektheit der Abgabe getroffen werden."
    elif(result[0] != "EQ"):
        return "\n\nDeine Lösung stimmt nicht mit der Musterlösung überein."
    return ""

