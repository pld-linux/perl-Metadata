#
# Conditional build:
# _without_tests - do not perform "make test"
%include	/usr/lib/rpm/macros.perl
%define	pdir	Metadata
Summary:	Metadata - classes for simple metadata
Summary(pl):	Metadata - klasy dla prostych metadanych
Name:		perl-Metadata
Version:	0.24
Release:	4
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{version}.tar.gz
Patch0:		%{name}.patch
BuildRequires:	perl >= 5.005_03-10
%if %{?_without_tests:0}%{!?_without_tests:1}
BuildRequires:	perl-TimeDate
%endif
Requires:	perl-TimeDate
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This collection of modules provide an implementation of Dublin Core
compatible metadata and subclasses for IAFA Templates, SOIF (Harvest)
and should be easily extendible to similar (fairly flat) metadata
formats.

# %description -l pl
# TODO

%prep
%setup -q -n Metadata-%{version}
%patch -p1

%build
perl Makefile.PL
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
install examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BUGS Changes README
%{perl_sitelib}/Metadata
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
