{
  description = "A very basic flake";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-23.11";
    flake-utils.url = "github:numtide/flake-utils";
    pyproject-nix.url = "github:nix-community/pyproject.nix";
  };

  outputs =
    {
      self,
      nixpkgs,
      flake-utils,
      pyproject-nix,
    }:
    flake-utils.lib.eachDefaultSystem (
      system:
      let
        pkgs = nixpkgs.legacyPackages.${system};
        snakeGamePy = pkgs.callPackage ./snakegame.nix { inherit pyproject-nix; };
      in
      {
        # devShell = pkgs.mkShell {
        #   packages = with pkgs; [ (python311.withPackages (ps: [ ps.pygame ])) ];
        # };
        devShell = {
          py = snakeGamePy.devShell;
        };
        packages = rec {
          py = snakeGamePy.package;
        };
      }
    );
  # let
  #   pkgs = nixpkgs.legacyPackges.x86_64-linux;
  # in
  # {
  #   # devShell.x86_64-linux = import ./shell.nix { inherit nixpkgs; };
  #   # packages.x86_64-linux.default = import ./default.nix { inherit nixpkgs; };
  # };
}
