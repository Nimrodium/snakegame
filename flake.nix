{
  description = "A very basic flake";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
    naersk.url = "github:nix-community/naersk";
    naersk.inputs.nixpkgs.follows = "nixpkgs"; # rust builder
  };

  outputs =
    {
      self,
      nixpkgs,
      flake-utils,
      naersk,
    }:
    flake-utils.lib.eachDefaultSystem (
      system:
      let
        pkgs = nixpkgs.legacyPackages.${system};
        snakeGamePy = pkgs.callPackage ./py/snakegame.nix { };
        snakeGameRs = pkgs.callPackage ./rs/snakegame.nix { inherit naersk; };
        snakeGameJava = pkgs.callPackage ./java/snakegame.nix { };
      in
      {
        # later make a function that just populates this from an attribute set of all the snakegame.nixes,
        # i guess this would be map to (devshell,package) -> and then fold over devShell and package attribute set, returning the final
        devShells = {
          py = snakeGamePy.devShell;
          rs = snakeGameRs.devShell;
          java = snakeGameJava.devShell;
        };
        packages = rec {
          py = snakeGamePy.package;
          rs = snakeGameRs.package;
        };
      }
    );
}
