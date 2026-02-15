{ pkgs, naersk, ... }:
let
  naersk' = pkgs.callPackage naersk { };
  nativeBuildInputs = with pkgs; [ sdl3 ];
in
{
  package = naersk'.buildPackage {
    src = ./.;
    inherit nativeBuildInputs;
    pname = "snakegame-rs";
	
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
