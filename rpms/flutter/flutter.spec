

Name:           flutter
Version:        2.2.3
Release:        2%{?dist}
Summary:        Flutter mobile app development framework.

License:        BSD
URL:            https://flutter.dev/
Source0:        https://github.com/flutter/flutter/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  bash
BuildRequires:  curl
BuildRequires:  git
BuildRequires:  zip
BuildRequires:  unzip

%description
The Flutter mobile app development framework.
Flutter allows developers to make cross-platform mobile apps with ease.

%prep
%autosetup -n %{name}-%{version}

%install
mkdir -p %{buildroot}/opt/%{name}/
cp -r %{_builddir}/%{name}-%{version}/* %{buildroot}/opt/%{name}/

mkdir -p  %{buildroot}%{_sysconfdir}/profile.d/

touch %{buildroot}%{_sysconfdir}/profile.d/%{name}.sh
cat > %{buildroot}%{_sysconfdir}/profile.d/%{name}.sh <<-EOF
export FLUTTER_HOME=/opt/flutter
export PATH=\${PATH}:\${FLUTTER_HOME}/bin
EOF

touch %{buildroot}%{_sysconfdir}/profile.d/%{name}.csh
cat > %{buildroot}%{_sysconfdir}/profile.d/%{name}.csh <<-EOF
setenv FLUTTER_HOME /opt/flutter
setenv PATH \${PATH}:\${FLUTTER_HOME}/bin:
EOF

%files
/opt/flutter/*
%{_sysconfdir}/profile.d/%{name}.sh
%{_sysconfdir}/profile.d/%{name}.csh


%license LICENSE
%doc README.md

%changelog

* Wed Aug 18 2021 Christopher Crouse <mail@amz-x.com>
- Updated spec file

* Sun Jul 18 2021 Christopher Crouse <mail@amz-x.com>
- Initialized spec file