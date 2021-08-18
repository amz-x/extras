

Name:           flutter
Version:        2.2.3
Release:        4%{?dist}
Summary:        Flutter mobile app development framework.

License:        BSD
URL:            https://flutter.dev/
Source0:        https://storage.googleapis.com/flutter_infra_release/releases/stable/linux/%{name}_linux_%{version}-stable.tar.xz#/%{name}-%{version}.tar.xz

BuildRequires:  bash
BuildRequires:  curl
BuildRequires:  git
BuildRequires:  zip
BuildRequires:  unzip

Requires:       glibc
Requires:       glibc-devel
Requires:       libglvnd-egl
Requires:       libglvnd-devel

%description
The Flutter mobile app development framework.
Flutter allows developers to make cross-platform mobile apps with ease.

%prep
tar -xf %{_sourcedir}/%{name}-%{version}.tar.xz

%install
mkdir -p %{buildroot}/opt/%{name}/
cp -r %{_builddir}/%{name}/* %{buildroot}/opt/%{name}/
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

%changelog

* Wed Aug 18 2021 Christopher Crouse <mail@amz-x.com>
- Updated file

* Sun Jul 18 2021 Christopher Crouse <mail@amz-x.com>
- Initialized spec file