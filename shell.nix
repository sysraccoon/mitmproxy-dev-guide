{ pkgs ? import <nixpkgs> {} }:

with pkgs; mkShell {
    name = "example-env";

    buildInputs = [
      python39
      python39Packages.venvShellHook
      autoPatchelfHook
    ];

    propagatedBuildInputs = [
      stdenv.cc.cc.lib
    ];

    venvDir = "./venv";
    postVenvCreation = ''
      unset SOURCE_DATE_EPOCH
      pip3 install -U pip setuptools wheel
      pip3 install -r requirements.txt
      autoPatchelf ./venv
    '';

    postShellHook = ''
    # set SOURCE_DATE_EPOCH so that we can use python wheels
    export SOURCE_DATE_EPOCH=315532800
    unset LD_LIBRARY_PATH
    '';
    preferLocalBuild = true;
}
