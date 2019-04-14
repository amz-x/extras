%define debug_package %{nil}
%define app_name pvpn

Name:           protonvpn-cli
Version:        1.1.2
Release:        1%{?dist}
Summary:        ProtonVPN CLI

License:        MIT
URL:            https://github.com/ProtonVPN/%{name}
Source0:        %{url}/archive/v%{version}.tar.gz

Requires:       openvpn
Requires:       python3
Requires:       dialog
Requires:       wget

BuildRequires:  git

%description
ProtonVPN CLI is a command-line tool for Linux and macOS.

%prep

%autosetup

%build

%install
mkdir -p "%{buildroot}/usr/bin"
install -m 0755 "%{name}.sh" "%{buildroot}/usr/bin/%{name}"
ln -sf "%{name}.sh" "%{buildroot}/usr/bin/%{app_name}"

%files
%{_bindir}/%{name}
%{_bindir}/%{app_name}

%license license.md
%doc README.md

%changelog
* Mon Apr 1 2019 Christopher Crouse <amz.x@protonmail.com>
- Initialized spec file

* Sun Apr 14 2019 Christopher Crouse <amz.x@protonmail.com>
- Update protonvpn-cli spec