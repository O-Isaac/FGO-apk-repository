import os
import subprocess
import platform


def subprocess_log(process):
    if process.returncode == 1:
        print(process.stderr)
    else:
        print(process.stdout)


def install_protoc_linux():
    # https://grpc.io/docs/protoc-installation/ - Install pre-compiled binaries (any OS)
    # Is the best way to ensure is protoc installed
    github_releases = "https://github.com/protocolbuffers/protobuf/releases"
    version_release = "/download/v3.15.8/protoc-3.15.8-linux-x86_64.zip"
    zip_name = "protoc-3.15.8-linux-x86_64.zip"

    download = subprocess.run(f"curl -LO {github_releases}{version_release}", shell=True, capture_output=True)
    subprocess_log(download)

    unzip_file = subprocess.run(f"unzip {zip_name} -d $HOME/.local", shell=True, capture_output=True)
    subprocess_log(unzip_file)

    update_env = subprocess.run(f'export PATH="$PATH:$HOME/.local/bin"', shell=True, capture_output=True)
    subprocess_log(update_env)


def install_protoc_windows():
    choco_version = subprocess.run("choco --version", shell=True, capture_output=True)

    if choco_version.returncode == 0:
        choco_output = subprocess.run("choco install protoc", shell=True, capture_output=True)
        subprocess_log(choco_output)
    else:
        print("[!] Chocolatey is not installed in system please go to https://chocolatey.org/install.")


def main():
    o_system = platform.system()

    print("[📦] Installing protoc")
    if o_system == "Linux":
        install_protoc_linux()
    else:
        install_protoc_windows()
    print("[📦] protoc successfully installed.")


if __name__ == "__main__":
    main()
