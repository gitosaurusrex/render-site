{ pkgs }: {
  deps = [
    pkgs.postgresql_15
    pkgs.postgresql
    pkgs.openssl
    pkgs.nodePackages.vscode-langservers-extracted
    pkgs.nodePackages.typescript-language-server  
  ];
  env = {
    PYTHON_LD_LIBRARY_PATH = pkgs.lib.makeLibraryPath [
      pkgs.postgresql
    ];
  };
}