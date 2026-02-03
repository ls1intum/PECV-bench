package de.tum.in.ase;

import de.tum.in.test.api.*;
import java.lang.annotation.*;
import static java.lang.annotation.RetentionPolicy.RUNTIME;
import static java.lang.annotation.ElementType.*;

@WhitelistPath(value = "../testinfunexam24e01v01**", type = PathType.GLOB) // for manual assessment and development
@WhitelistPath("target") // mainly for Artemis
@WhitelistClass(BehaviorTest.class)
@WhitelistClass(HelperClass.class)
@BlacklistPath(value = "{build/classes/java/test,test}/**.{java,class,json}", type = PathType.GLOB)
@StrictTimeout(5)
@MirrorOutput
@Retention(RUNTIME)
@Target({TYPE, ANNOTATION_TYPE})
@Deadline("2024-12-13 10:40 Europe/Berlin")
@ActivateHiddenBefore("2024-12-13 10:40 Europe/Berlin")
public @interface E01V01 {
}
