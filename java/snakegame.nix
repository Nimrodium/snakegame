{ pkgs, ... }:

{
  devShell = pkgs.mkShell {
    nativeBuildInputs = with pkgs; [
      java-language-server
      openjdk25
    ];
  };
  package = { };
}
