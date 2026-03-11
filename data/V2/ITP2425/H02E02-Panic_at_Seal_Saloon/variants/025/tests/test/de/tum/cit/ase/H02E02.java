package de.tum.cit.ase;

import de.tum.in.test.api.*;

import java.lang.annotation.Retention;
import java.lang.annotation.Target;

import static java.lang.annotation.ElementType.ANNOTATION_TYPE;
import static java.lang.annotation.ElementType.TYPE;
import static java.lang.annotation.RetentionPolicy.RUNTIME;

@WhitelistPath(value = "../testprog23h02e02**", type = PathType.GLOB) // for manual assessment and development
@WhitelistPath("target") // mainly for Artemis
@WhitelistClass(AttributeHelper.class)
@WhitelistClass(BehaviorTest.class)
@BlacklistPath(value = "{build/classes/java/test,test}/**.{java,class,json}", type = PathType.GLOB)
@StrictTimeout(5)
@MirrorOutput
@Retention(RUNTIME)
@Target({ TYPE, ANNOTATION_TYPE })
public @interface H02E02 {
}
