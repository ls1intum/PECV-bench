package de.tum.in.ase.eist;

import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;

import de.tum.in.test.api.*;
import de.tum.in.test.api.jupiter.JupiterIOExtension;
import de.tum.in.test.api.jupiter.JupiterStrictTimeoutExtension;
import org.junit.jupiter.api.extension.ExtendWith;

@ExtendWith(JupiterIOExtension.class)
@ExtendWith(JupiterStrictTimeoutExtension.class)
@StrictTimeout(6)
@Retention(RetentionPolicy.RUNTIME)
public @interface H05E01 {
    // marker
}
