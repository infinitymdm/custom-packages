Name:           micro
Version:        2.0.11
Release:        1.osu%{?dist}
Summary:        A modern and intuitive terminal-based text editor

License:        MIT
URL:            https://github.com/zyedidia/%{name}
Source0:        https://github.com/zyedidia/%{name}/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  golang
Requires:       xclip xsel

%description
A modern and intuitive terminal-based text editor

%prep
%setup -q


%build
%define debug_package %{nil}
make %{?_smp_mflags}


%install
install -Dm00755 %{name} %{buildroot}%{_bindir}/%{name}
install -Dm00644 assets/packaging/%{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1


%files
%{_bindir}/micro
%doc %{_mandir}/man*/%{name}*


%changelog
* Tue Aug 01 2023 Marcus Mellor <marcus.mellor@okstate.edu> - 2.0.11-1.osu
- First micro package for OSU research cluster
