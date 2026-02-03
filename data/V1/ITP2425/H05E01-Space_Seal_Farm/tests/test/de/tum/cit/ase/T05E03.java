package de.tum.cit.ase;

import de.tum.in.test.api.*;

import java.lang.annotation.Retention;
import java.lang.annotation.Target;

import static java.lang.annotation.ElementType.ANNOTATION_TYPE;
import static java.lang.annotation.ElementType.TYPE;
import static java.lang.annotation.RetentionPolicy.RUNTIME;

@WhitelistPath(value = "../testprog23h04e01**", type = PathType.GLOB)
@BlacklistPath(value = "{build/classes/java/test,test}/**.{java,class,json}", type = PathType.GLOB)
@StrictTimeout(10)
@WhitelistClass(AttributeHelper.class)
@MirrorOutput
@Retention(RUNTIME)
@Target({TYPE, ANNOTATION_TYPE})
public @interface T05E03 {
}
