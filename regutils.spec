Summary:	Manipulate the Win9x registry
Name:		regutils
Version:	0.10
Release:	%mkrel 12
License:	GPL
Group:		Networking/Other
URL:		https://www.cs.mun.ca/~michael/regutils/
Source0:	%{name}-%{version}.tar.bz2
Patch0:		regutils-0.10-Makefile.patch
Requires:	findutils
#Requires:	samba-common samba
BuildRequires:	ed
BuildRequires:	perl
Provides:	regedit
Conflicts:	wine-utils
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%define _requires_exceptions perl\(regfilterLib\.pl\)

%description
Regutils is a collection of programs to help in installing dos/windows
software for diskless machines served by a unix machine. They are also
useful for applying user and machine specific customizations on the
fly as users log in, or as machines are booted.

%prep

%setup -q
%patch0 -p0

%build
%make

perl -pi -e 's#/local/bin/perl#%{_bindir}/perl#' apply-app-changes.*

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_libdir}
install -m 755 regedit %{buildroot}%{_bindir}/
install -m 755 regdiff.pl %{buildroot}%{_bindir}/regdiff
install -m 755 regfilter.pl %{buildroot}%{_bindir}/regfilter
install -m 755 reghexprint.pl %{buildroot}%{_bindir}/reghexprint
install -m 755 regsort.pl %{buildroot}%{_bindir}/regsort
install -m 755 inicat.pl %{buildroot}%{_bindir}/inicat
install -m 755 inidiff.pl %{buildroot}%{_bindir}/inidiff
install -m 755 iniedit.pl %{buildroot}%{_bindir}/iniedit
install -m 755 gen-app-changes.pl %{buildroot}%{_bindir}/gen-app-changes
install -m 755 apply-app-changes.pl %{buildroot}%{_bindir}/apply-app-changes
install -m 755 fix-w9x-lnk.pl %{buildroot}%{_bindir}/fix-w9x-lnk
install -m 644 regfilterLib.pl %{buildroot}%{_libdir}/
install -m 644 IniFile.pm %{buildroot}%{_libdir}/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc INSTALL NEWS PROJECTS README
%{_bindir}/*
%{_libdir}/*


%changelog
* Tue Sep 08 2009 Thierry Vignaud <tvignaud@mandriva.com> 0.10-12mdv2010.0
+ Revision: 433092
- rebuild

* Sun Jul 20 2008 Oden Eriksson <oeriksson@mandriva.com> 0.10-11mdv2009.0
+ Revision: 239034
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Sep 19 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.10-10mdv2008.0
+ Revision: 90251
- rebuild


* Fri Jan 12 2007 Andreas Hasenack <andreas@mandriva.com> 0.10-9mdv2007.0
+ Revision: 108024
- rebuild
- using mkrel
- Import regutils

* Sun Dec 25 2005 Oden Eriksson <oeriksson@mandriva.com> 0.10-8mdk
- fix wrong-script-interpreter

* Sun Dec 25 2005 Oden Eriksson <oeriksson@mandriva.com> 0.10-7mdk
- rebuild

* Sat Oct 16 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 0.10-6mdk
- rebuilt
- rename patch

