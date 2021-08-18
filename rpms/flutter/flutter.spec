Name:           flutter
Version:        2.2.3
Release:        5%{?dist}
Summary:        Flutter mobile app development framework.

License:        BSD
URL:            https://flutter.dev/
Source0:        https://storage.googleapis.com/flutter_infra_release/releases/stable/linux/%{name}_linux_%{version}-stable.tar.xz#/%{name}-%{version}.tar.xz

AutoReq:        no

BuildRequires:  rsync

BuildRequires:  rpmlib(CompressedFileNames) <= 3.0.4-1
BuildRequires:  rpmlib(FileDigests) <= 4.6.0-1
BuildRequires:  rpmlib(PayloadFilesHavePrefix) <= 4.0-1

Requires:       bash
Requires:       git
Requires:       unzip
Requires:       zip


# Mesa packages
Requires:       mesa-libEGL
Requires:       mesa-libEGL-devel
Requires:       mesa-libGL
Requires:       mesa-libGL-devel
Requires:       mesa-libGLU
Requires:       mesa-libGLU-devel

##
# Requirements list generated
#
# Requires:       /bin/sh
# Requires:       /usr/bin/bash
# Requires:       /usr/bin/sh
# Requires:       ld-linux-x86-64.so.2()(64bit)
# Requires:       ld-linux-x86-64.so.2(GLIBC_2.3)(64bit)
# Requires:       libEGL.so
# Requires:       libEGL.so()(64bit)
# Requires:       libGLESv2.so
# Requires:       libGLESv2.so()(64bit)
# Requires:       libandroid.so 
# Requires:       libandroid.so()(64bit)
# Requires:       libatk-1.0.so.0()(64bit)
# Requires:       libc.so
# Requires:       libc.so()(64bit)
# Requires:       libc.so(LIBC)
# Requires:       libc.so(LIBC)(64bit)
# Requires:       libc.so.6()(64bit) 
# Requires:       libc.so.6(GLIBC_2.14)(64bit)
# Requires:       libc.so.6(GLIBC_2.16)(64bit)
# Requires:       libc.so.6(GLIBC_2.17)(64bit)
# Requires:       libc.so.6(GLIBC_2.2.5)(64bit)
# Requires:       libc.so.6(GLIBC_2.3)(64bit)
# Requires:       libc.so.6(GLIBC_2.3.2)(64bit)
# Requires:       libc.so.6(GLIBC_2.3.3)(64bit)
# Requires:       libc.so.6(GLIBC_2.3.4)(64bit)
# Requires:       libc.so.6(GLIBC_2.4)(64bit)
# Requires:       libc.so.6(GLIBC_2.6)(64bit)
# Requires:       libc.so.6(GLIBC_2.7)(64bit)
# Requires:       libc.so.6(GLIBC_2.8)(64bit)
# Requires:       libc.so.6(GLIBC_2.9)(64bit)
# Requires:       libdl.so
# Requires:       libdl.so()(64bit)
# Requires:       libdl.so(LIBC)
# Requires:       libdl.so(LIBC)(64bit)
# Requires:       libdl.so.2()(64bit)
# Requires:       libdl.so.2(GLIBC_2.2.5)(64bit)
# Requires:       libepoxy.so.0()(64bit)
# Requires:       libgdk-3.so.0()(64bit)
# Requires:       libgio-2.0.so.0()(64bit)
# Requires:       libglib-2.0.so.0()(64bit)
# Requires:       libgobject-2.0.so.0()(64bit)
# Requires:       libgtk-3.so.0()(64bit)
# Requires:       liblog.so
# Requires:       liblog.so()(64bit)
# Requires:       libm.so
# Requires:       libm.so()(64bit)
# Requires:       libm.so(LIBC)
# Requires:       libm.so(LIBC)(64bit)
# Requires:       libm.so.6()(64bit)
# Requires:       libm.so.6(GLIBC_2.2.5)(64bit)
# Requires:       libpthread.so.0()(64bit) 
# Requires:       libpthread.so.0(GLIBC_2.12)(64bit)
# Requires:       libpthread.so.0(GLIBC_2.2.5)(64bit)
# Requires:       libpthread.so.0(GLIBC_2.3.2)(64bit)
# Requires:       libpthread.so.0(GLIBC_2.3.3)(64bit)

%description
The Flutter mobile app development framework.
Flutter allows developers to make cross-platform mobile apps with ease.

%prep
tar -xf %{_sourcedir}/%{name}-%{version}.tar.xz

%install
mkdir -p %{buildroot}/opt/%{name}/
rsync -rtv %{_builddir}/%{name}/ %{buildroot}/opt/%{name}/

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
/opt/flutter/.*

%{_sysconfdir}/profile.d/%{name}.sh
%{_sysconfdir}/profile.d/%{name}.csh


%changelog

* Wed Aug 18 2021 Christopher Crouse <mail@amz-x.com>
- Updated file

* Sun Jul 18 2021 Christopher Crouse <mail@amz-x.com>
- Initialized spec file