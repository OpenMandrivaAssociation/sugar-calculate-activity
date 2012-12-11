# NOTE: Do not edit, file was generated by jhconvert

Name: sugar-calculate-activity
Version: 30
Release: %mkrel 1
Summary: Calculate activity for Sugar
License: GPLv2+
Group: Graphical desktop/Other
Url: http://sugarlabs.org/

Source: http://download.sugarlabs.org/sources/sucrose/fructose/Calculate/Calculate-30.tar.bz2

Requires: sugar-toolkit >= 0.85.3

BuildRequires: gettext  
BuildRequires: sugar-toolkit >= 0.85.3

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch: noarch

%description
The calculate activity provides a generic calculator.
The interface provides the simplest functions directly and should therefore
be easy to usen for the youngest children. However, it does support more
complicated math and variables.

%prep
%setup -q -n Calculate-30


%build

rm -f MANIFEST
python setup.py build

%install
rm -rf %{buildroot}
python setup.py install --prefix=%{buildroot}/%{_prefix}
find %{buildroot} -name '*.py.orig' -print0 | xargs -0 rm -f
%find_lang org.laptop.Calculate

%clean
rm -rf %{buildroot}

%files -f org.laptop.Calculate.lang
%defattr(-,root,root,-)
%{_datadir}/sugar/activities/*
%doc NEWS AUTHORS COPYING



%changelog
* Tue Aug 11 2009 Aleksey Lim <alsroot@mandriva.org> 30-1mdv2010.0
+ Revision: 414898
- Sucrose 0.85.2

* Tue Jan 20 2009 Aleksey Lim <alsroot@mandriva.org> 28-1mdv2009.1
+ Revision: 331983
- new Sucrose 0.83.4 release

* Sun Jan 11 2009 Aleksey Lim <alsroot@mandriva.org> 26-1mdv2009.1
+ Revision: 328375
- Sugar 0.83.3 release

  + Bogdano Arendartchuk <bogdano@mandriva.com>
    - import sugar-calculator


* Tue Sep  2 2008 Jeremy Katz <katzj@redhat.com> - 23-1
- update to Calculate-23
- use %%find_lang 

* Thu Jul 31 2008 Jeremy Katz <katzj@redhat.com> - 19-1
- Initial packaging
