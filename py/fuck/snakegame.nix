{ pkgs, pyproject-nix, ... }:
# I cannot use uv2nix. i cannot package this as a python package.
# pygame refuses to use a real driver unless i directly use pkgs.python311.pythonPackages.pygame.
# which i can only use if i directly run python ./src/main.py
# fuck you pygame. fuck you nix. fuck you uv. fuck you pyproject-nix. fuck you buildPythonApplication. but especially. fuck you python.
# i wasted 5 hours on this.
let
  python = pkgs.python311;
  py = (python.withPackages (ps: [ ps.pygame ]));
in
{
  devShell = pkgs.mkShell {
    packages = [
      py
      pkgs.fish
    ];
    runScript = "fish";
  };
  package = pkgs.writeShellScriptBin "snakegame" ''
    PYTHONPATH=${./src} exec ${py}/bin/python ${./src/main.py}
  '';
}
