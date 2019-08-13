%define debug_package %{nil}

Name:           php-version
Version:        0.13.0
Release:        1%{?dist}
Summary:        Exposes a php-version command allowing developers to switch between versions of PHP

License:        MIT
URL:            https://github.com/wilmoore/%{name}
Source0:        %{url}/archive/%{version}.tar.gz

BuildRequires:  git

%description
%{summary}.

%prep

%autosetup

%build

%install
mkdir -p "%{buildroot}/usr/bin"
install -m 0755 "%{name}.sh" "%{buildroot}/usr/bin/%{name}"

%files
%{_bindir}/%{name}

%license LICENSE
%doc README.md

%changelog
* Tue Aug 13 2019 Christopher Crouse <mail@amz-x.com>
- Initialized spec file