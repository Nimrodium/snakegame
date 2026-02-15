{ pkgs, ... }:

{
  devShell = pkgs.mkShell {
    nativeBuildInputs = with pkgs; [
      java-language-server
      openjdk21
      gradle
      sdl2-compat
    ];
  };
  package = { };
}
