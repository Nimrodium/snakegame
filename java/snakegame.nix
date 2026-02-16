{ pkgs, lib, ... }:

let
  nativeBuildInputs = with pkgs; [
    openjdk21
    gradle
  ];
in
{
  devShell = pkgs.mkShell {
    inherit nativeBuildInputs;
  };
  package = pkgs.stdenv.mkDerivation {
    pname = "snakegame-java";
    version = "0.1";
    src = ./.;
    inherit nativeBuildInputs;
    buildPhase = ''
      gradle build :app:installDist --no-daemon
    '';
    installPhase = ''
      # ls $out
      mkdir -p $out
      cp -r app/build/install/snakegame-java/bin $out/bin
      cp -r app/build/install/snakegame-java/lib $out/lib
    '';
  };
}
