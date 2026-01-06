package de.tum.in.ase;

import de.tum.in.test.api.*;
import java.lang.annotation.*;
import static java.lang.annotation.RetentionPolicy.RUNTIME;
import static java.lang.annotation.ElementType.*;

@WhitelistPath(value = "../testinfunexam23e01v01**", type = PathType.GLOB) // for manual assessment and development
@WhitelistPath("target") // mainly for Artemis
@WhitelistClass(BehaviorTest.class)
@WhitelistClass(HelperClass.class)
@BlacklistPath(value = "{build/classes/java/test,test}/**.{java,class,json}", type = PathType.GLOB)
@StrictTimeout(5)
@MirrorOutput
@Retention(RUNTIME)
@Target({TYPE, ANNOTATION_TYPE})
@Deadline("2023-02-28 20:00 Europe/Berlin")
@ActivateHiddenBefore("2023-02-28 18:00 Europe/Berlin")
public @interface E01V01 {
}
