%include	/usr/lib/rpm/macros.perl
Summary:	Metadata perl module
Summary(pl):	Modu³ perla Metadata
Name:		perl-Metadata
Version:	0.24
Release:	3
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Metadata/Metadata-%{version}.tar.gz
Patch0:		%{name}.patch
BuildRequires:	perl >= 5.005_03-10
BuildRequires:	perl-TimeDate
Requires:	perl-TimeDate
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Metadata set of modules.

%description -l pl
Zestaw modu³ów Metadata.

%prep
%setup -q -n Metadata-%{version}
%patch -p1

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

gzip -9nf Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/Metadata
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
