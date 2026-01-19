{ pkgs, naersk, ... }:
let
  naersk' = pkgs.callPackage naersk { };
  nativeBuildInputs = with pkgs; [ sdl3 ];
in
rec {
  package = naersk'.buildPackage {
    src = ./.;
    inherit nativeBuildInputs;
  };
  devShell = pkgs.mkShell {
    nativeBuildInputs =
      with pkgs;
      [
        rustc
        cargo
      ]
      ++ nativeBuildInputs;
  };

}
