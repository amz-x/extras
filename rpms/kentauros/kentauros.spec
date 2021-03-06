Name:           kentauros
Summary:        Modular, automatic and configurable package build system
Version:        1.0.7
Release:        3%{?dist}
License:        GPLv2

URL:            https://github.com/decathorpe/%{name}
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-GitPython
BuildRequires:  python3-argcomplete
BuildRequires:  python3-devel >= 3.5
BuildRequires:  python3-tinydb

Requires:       python3-GitPython
Requires:       python3-argcomplete
Requires:       python3-tinydb

Recommends:     python3-ujson

Recommends:     createrepo_c
Recommends:     copr-cli
Recommends:     git
Recommends:     mock
Recommends:     rpmdevtools
Recommends:     rpmlint
Recommends:     wget


%description
kentauros is a small build system with little need for configuration.
create a directory named after the project, drop in a .conf and RPM
.spec file, configure copr-cli, and automagic updating, building,
uploading to copr works.


%prep
%autosetup


%build
%py3_build


%install
%py3_install


%files
%{_bindir}/ktr

%{_datadir}/kentauros/default.conf
%{_datadir}/kentauros/template.conf

%{python3_sitelib}/kentauros
%{python3_sitelib}/kentauros-%{version}-py%{python3_version}.egg-info/


%changelog
* Fri Jul 09 2021 Christopher Crouse <mail@amz-x.com> - 1.0.7-3
- Update files section.

* Fri Jul 09 2021 Christopher Crouse <mail@amz-x.com> - 1.0.7-2
- Imported spec.

* Sat May 27 2017 Fabio Valentini <decathorpe@gmail.com> - 1.0.7-1
- Update to version 1.0.7.

* Fri May 26 2017 Fabio Valentini <decathorpe@gmail.com> - 1.0.6-1
- Update to version 1.0.6.

* Sun May 14 2017 Fabio Valentini <decathorpe@gmail.com> - 1.0.5-1
- Update to version 1.0.5.

* Fri May 12 2017 Fabio Valentini <decathorpe@gmail.com> - 1.0.4-1
- Update to version 1.0.4.

* Sun Apr 30 2017 Fabio Valentini <decathorpe@gmail.com> - 1.0.3-1
- Update to version 1.0.3.

* Fri Apr 21 2017 Fabio Valentini <decathorpe@gmail.com> - 1.0.2-1
- Update to version 1.0.2.

* Wed Jan 18 2017 Fabio Valentini <decathorpe@gmail.com> - 1.0.1-1
- Update to version 1.0.1.

* Mon Jan 16 2017 Fabio Valentini <decathorpe@gmail.com> - 1.0.0-1
- Update to version 1.0.0.

* Sat Jan 14 2017 Fabio Valentini <decathorpe@gmail.com> - 0.9.109-1
- Update to version 0.9.109.

* Thu Jan 05 2017 Fabio Valentini <decathorpe@gmail.com> - 0.9.108-1
- Update to version 0.9.108.

* Wed Jan 04 2017 Fabio Valentini <decathorpe@gmail.com> - 0.9.107-1
- Update to version 0.9.107.

* Tue Jan 03 2017 Fabio Valentini <decathorpe@gmail.com> - 0.9.106-1
- Update to version 0.9.106.

* Mon Jan 02 2017 Fabio Valentini <decathorpe@gmail.com> - 0.9.105-1
- Update to version 0.9.105.

* Mon Jan 02 2017 Fabio Valentini <decathorpe@gmail.com> - 0.9.104-1
- Update to version 0.9.104.

* Sun Jan 01 2017 Fabio Valentini <decathorpe@gmail.com> - 0.9.103-1
- Update to version 0.9.103.

* Sat Dec 31 2016 Fabio Valentini <decathorpe@gmail.com> - 0.9.102-1
- Update to version 0.9.102.

* Sat Dec 31 2016 Fabio Valentini <decathorpe@gmail.com> - 0.9.101-1
- Update to version 0.9.101.

* Fri Dec 30 2016 Fabio Valentini <decathorpe@gmail.com> - 0.9.100-1
- Update to version 0.9.100.

* Fri Dec 30 2016 Fabio Valentini <decathorpe@gmail.com> - 0.9.99-1
- Update to version 0.9.99.

* Fri Dec 30 2016 Fabio Valentini <decathorpe@gmail.com> - 0.9.98.1-1
- Update to version 0.9.98.1.

* Thu Dec 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.9.98-1
- Update to version 0.9.98.

* Thu Dec 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.9.97-1
- Update to version 0.9.97.

* Thu Dec 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.9.96.1-1
- Update to version 0.9.96.1.

* Thu Dec 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.9.96-1
- Update to version 0.9.96.

* Thu Dec 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.9.95-1
- Update to version 0.9.95

* Wed Dec 28 2016 Fabio Valentini <decathorpe@gmail.com> - 0.9.94-1
- Update to version 0.9.94.

* Wed Dec 28 2016 Fabio Valentini <decathorpe@gmail.com> - 0.9.93-2
- Recommend python3-ujson.

* Wed Dec 28 2016 Fabio Valentini <decathorpe@gmail.com> - 0.9.93-1
- Update to version 0.9.93.

* Wed Dec 28 2016 Fabio Valentini <decathorpe@gmail.com> - 0.9.92-1
- Update to version 0.9.92.

* Wed Dec 28 2016 Fabio Valentini <decathorpe@gmail.com> - 0.9.91-1
- Update to version 0.9.91.

* Tue Dec 27 2016 Fabio Valentini <decathorpe@gmail.com> - 0.9.90-1
- Update to version 0.9.90.

* Fri Dec 23 2016 Fabio Valentini <decathorpe@gmail.com> - 0.9.15-1
- Update to version 0.9.15.
- Remove deprecated check scriptlet.

* Sat Oct 08 2016 Fabio Valentini <decathorpe@gmail.com> - 0.9.14-1
- Update to version 0.9.14.

* Thu Sep 22 2016 Fabio Valentini <decathorpe@gmail.com> - 0.9.13-1
- Update to version 0.9.13.

* Wed Sep 21 2016 Fabio Valentini <decathorpe@gmail.com> - 0.9.12-1
- Update to version 0.9.12.

* Mon May 09 2016 Fabio Valentini <decathorpe@gmail.com> - 0.9.11-1
- Update to version 0.9.11.

* Sat May 07 2016 Fabio Valentini <decathorpe@gmail.com> - 0.9.10.6-2
- Make package noarch.

* Sat May 07 2016 Fabio Valentini <decathorpe@gmail.com> - 0.9.10.6-1
- Update to version 0.9.10.6.

* Wed May 04 2016 Fabio Valentini <decathorpe@gmail.com> - 0.9.10.5-1
- Update to version 0.9.10.5.

* Mon May 02 2016 Fabio Valentini <decathorpe@gmail.com> - 0.9.10.4-1
- Update to version 0.9.10.4.

* Mon May 02 2016 Fabio Valentini <decathorpe@gmail.com> - 0.9.10.3-1
- Update to version 0.9.10.3.

* Mon May 02 2016 Fabio Valentini <decathorpe@gmail.com> - 0.9.10.2-1
- Update to version 0.9.10.2.

* Mon May 02 2016 Fabio Valentini <decathorpe@gmail.com> - 0.9.10.1-1
- Update to version 0.9.10.1.

* Fri Apr 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.9.10-1
- Update to version 0.9.10.

* Sat Apr 23 2016 Fabio Valentini <decathorpe@gmail.com> - 0.9.8-3
- Release bump for small fix.

* Sat Apr 23 2016 Fabio Valentini <decathorpe@gmail.com> - 0.9.8-2
- Release bump for small fix.

* Sat Apr 23 2016 Fabio Valentini <decathorpe@gmail.com> - 0.9.8-1
- Update to version 0.9.8.

* Sat Apr 23 2016 Fabio Valentini <decathorpe@gmail.com> - 0.9.7-1
- Update to version 0.9.7.

* Thu Apr 21 2016 Fabio Valentini <decathorpe@gmail.com> - 0.9.6-1
- Update to version 0.9.6.

* Wed Apr 20 2016 Fabio Valentini <decathorpe@gmail.com> - 0.9.5-5
- Version bump for some fixes.

* Mon Apr 18 2016 Fabio Valentini <decathorpe@gmail.com> - 0.9.5-4
- Version bump for small fix.

* Sat Apr 16 2016 Fabio Valentini <decathorpe@gmail.com> - 0.9.5-3
- Version bump for small fix.

* Fri Apr 15 2016 Fabio Valentini <decathorpe@gmail.com> - 0.9.5-2
- Version bump for small fix.

* Fri Apr 15 2016 Fabio Valentini <decathorpe@gmail.com> - 0.9.5-1
- Fix spec for new version.

* Fri Mar 11 2016 Fabio Valentini <decathorpe@gmail.com> - 0.9.3.2-1
- Bump to version 0.9.3.2.

* Fri Mar 11 2016 Fabio Valentini <decathorpe@gmail.com> - 0.9.3.1-1
- Bump to version 0.9.3.1.

* Fri Mar 11 2016 Fabio Valentini <decathorpe@gmail.com> - 0.9.3-1
- Bump to version 0.9.3.

* Sun Mar 06 2016 Fabio Valentini <decathorpe@gmail.com> - 0.9.2-1
- Bump to version 0.9.2.
- Move bzr, git, wget from Requires: to Recommends:
- Move rpmdevtools from Requires: to Suggests:
- They all are now detected at runtime.

* Wed Mar 02 2016 Fabio Valentini <decathorpe@gmail.com> - 0.9.1-1
- Bump to version 0.9.1.

* Wed Mar 02 2016 Fabio Valentini <decathorpe@gmail.com> - 0.9.0-2
- move copr-cli and mock from Requires: to Suggests:
- copr-cli and mock command presence is checked at runtime

* Sun Feb 28 2016 Fabio Valentini <decathorpe@gmail.com> - 0.9.0-1
- Bump to version 0.9.0.

* Wed Feb 24 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0-1
- Bump to version 0.1.0.

* Sat Jan 09 2016 Fabio Valentini <decathorpe@gmail.com> - 0.0.4-1
- Bump version to 0.0.4.

* Wed Dec 30 2015 Fabio Valentini <decathorpe@gmail.com> - 0.0.3-1
- Bump version to 0.0.3.

* Sun Dec 27 2015 Fabio Valentini <decathorpe@gmail.com> - 0.0.2-3
- Fix dep of main package on py3 package.

* Sat Dec 26 2015 Fabio Valentini <decathorpe@gmail.com> - 0.0.2-2
- Fix src.rpm package build with make-srpm.sh.

* Sat Dec 26 2015 Fabio Valentini <decathorpe@gmail.com> - 0.0.2-1
- Bump version for test release.

* Mon Oct 12 2015 Fabio Valentini <decathorpe@gmail.com> - 0.0.1-1
- Release 0.0.1.
