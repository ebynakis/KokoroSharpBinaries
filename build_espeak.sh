#!/bin/bash

cd espeak-ng

# Add pthread flags for Linux
if [[ "$(uname -s)" == "Linux" ]]; then
    EXTRA_CMAKE_ARGS="$EXTRA_CMAKE_ARGS -DCMAKE_C_FLAGS=-pthread -DCMAKE_EXE_LINKER_FLAGS=-pthread"
fi

# Build
cmake -B build -DBUILD_SHARED_LIBS=OFF -DENABLE_TESTS=OFF -DCOMPILE_INTONATIONS=OFF -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=_install . $EXTRA_CMAKE_ARGS
cmake --build build --config Release
cmake --install build

# Package
if [[ -f "_install/bin/espeak-ng.exe" ]]; then
    mv "_install/bin/espeak-ng.exe" "../espeak-ng.bin" # Windows
else
    chmod +x "_install/bin/espeak-ng"
    mv "_install/bin/espeak-ng" "../espeak-ng.bin"     # Unix
fi
