#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Metadata
Summary:	Metadata - classes for simple metadata
Summary(pl):	Metadata - klasy dla prostych metadanych
Name:		perl-Metadata
Version:	0.24
Release:	7
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{version}.tar.gz
# Source0-md5:	59fb764edce6681e85feb80decafb3fa
Patch0:		%{name}.patch
BuildRequires:	perl-devel >= 5.005_03-10
%if %{with tests}
BuildRequires:	perl-TimeDate
%endif
BuildRequires:	rpm-perlprov
Requires:	perl-TimeDate
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This collection of modules provide an implementation of Dublin Core
compatible metadata and subclasses for IAFA Templates, SOIF (Harvest)
and should be easily extendible to similar (fairly flat) metadata
formats.

%description -l pl
Ten zestaw modu³ów udostêpnia implementacjê zgodnych z Dublin Core
metadanych i podklas IAFA Templates i SOIF (Harvest). Powinny byæ
³atwo rozszerzalne do podobnych (p³askich) formatów metadanych.

%prep
%setup -q -n Metadata-%{version}
%patch -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
install examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BUGS Changes README
%{perl_vendorlib}/Metadata
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
