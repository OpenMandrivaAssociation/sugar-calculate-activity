Name: sugar-calculator
Version: 25
Release: 1%{?dist}
Summary: Calculator for Sugar
Group: Sugar/Activities
License: GPLv2+
URL: http://wiki.laptop.org/go/Calculate
Source0: http://dev.laptop.org/pub/sugar/sources/calculate-activity/Calculate-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  python sugar-toolkit
Requires: sugar
BuildArch: noarch

%description
The calculate activity provides a calculator for the Sugar interface.

%prep
%setup -q -n Calculate-%{version}

# remove bogus pseudo locale
rm -f po/pseudo.po

%build
python ./setup.py build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{sugaractivitydir}
python ./setup.py install --prefix=$RPM_BUILD_ROOT/%{_prefix}

%find_lang org.laptop.Calculate

%clean
rm -rf $RPM_BUILD_ROOT


%files -f org.laptop.Calculate.lang
%defattr(-,root,root,-)
%doc NEWS
%{sugaractivitydir}/Calculate.activity/


