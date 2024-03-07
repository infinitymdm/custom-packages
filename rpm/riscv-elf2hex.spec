Name:           riscv-elf2hex
Version:        20.08.00.00
Release:        1.osu${?dist}
Summary:        Converts ELF files to HEX files that are suitable for Verilog's readmemh

License:        BSD-3-Clause
URL:            https://riscv.org
Source0:        https://github.com/sifive/elf2hex/archive/revs/tags/v%{version}.tar.gz

BuildRequires:  riscv-gnu-toolchain

%description
Converts ELF files to HEX files that are suitable for Verilog's readmemh

%prep
%setup
autoreconf -i
./configure --target=riscv64-unknown-elf --prefix=$/opt/riscv

%build
%define debug_package %{nil}
make %{?_smp_mflags}

%install
make install

%files
TODO

%changelog
TODO
