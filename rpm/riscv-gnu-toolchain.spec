Name:           riscv-gnu-toolchain
Version:        2023.12.20
Release:        1.osu${?dist}
Summary:        GNU toolchain for RISC-V, including GCC

License:        GPL-2.0-or-later
URL:            https://riscv.org
Source0:        https://github.com/riscv-collab/%{name}/archive/revs/tags/%{version}.tar.gz

BuildRequires:  libmpc-devel mpfr-devel gmp-devel

%description
GNU toolchain for RISC-V, including GCC

%prep
%setup
./configure --enable-multilib --prefix=$/opt/riscv

%build
%define debug_package %{nil}
make %{?_smp_mflags}

%install
make install

%files
TODO

%changelog
TODO
