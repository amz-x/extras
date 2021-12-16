%define debug_package %{nil}

Name:           ruby-build
Version:        20211203
Release:        1%{?dist}
Summary:        A command-line utility, and a plugin to rbenv, that makes it easy to install virtually any version of ruby

BuildArch:      noarch
License:        MIT
URL:            https://github.com/rbenv/ruby-build
Source0:        https://github.com/rbenv/ruby-build/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz


%description
%{summary}.

%prep
%autosetup -n %{name}-%{version}

%install

mkdir -p "%{buildroot}%{_bindir}"
mkdir -p "%{buildroot}%{_datadir}/%{name}"

install -p bin/* "%{buildroot}%{_bindir}"
install -p -m 0644 share/ruby-build/* "%{buildroot}%{_datadir}/%{name}"

%files

%{_bindir}/%{name}

%{_bindir}/rbenv-install
%{_bindir}/rbenv-uninstall

%{_datadir}/%{name}/*

%license LICENSE
%doc README.md

%changelog

* Thu Dec 16 2021 Christopher Crouse <mail@amz-x.com>
- Init spec