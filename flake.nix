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
      in
      {
        # devShell = pkgs.mkShell {
        #   packages = with pkgs; [ (python311.withPackages (ps: [ ps.pygame ])) ];
        # };
        devShell = {
          py = snakeGamePy.devShell;
          rs = snakeGameRs.devShell;
        };
        packages = rec {
          py = snakeGamePy.package;
          rs = snakeGameRs.package;
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
