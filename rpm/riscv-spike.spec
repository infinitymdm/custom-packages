Name:           riscv-spike
Version:        1.1.0
Release:        1.osu%{?dist}
Summary:        A RISC-V ISA Simulator

License:        BSD-3-Clause
URL:            https://riscv.org
Source0:        https://github.com/riscv-software-src/riscv-isa-sim/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  dtc boost1.78-devel
Requires:       riscv-gnu-toolchain

%description
Spike, the RISC-V ISA Simulator, implements a functional model of one or more RISC-V harts. It is named after the golden spike used to celebrate the completion of the US transcontinental railway.

%prep
%setup -q
mkdir build
cd build
../configure --prefix=/opt/riscv

%build
%define debug_package %{nil}
make %{?_smp_mflags}


%install
make install

%files
TODO

%changelog
TODO
