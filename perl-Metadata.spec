%define		perl_sitelib	%(eval "`perl -V:installsitelib`"; echo $installsitelib)
Summary:	Metadata perl module
Summary(pl):	Modu³ perla Metadata
Name:		perl-Metadata
Version:	0.23
Release:	3
Copyright:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Metadata/Metadata-%{version}.tar.gz
Patch:		perl-Metadata.patch
BuildRequires:	perl >= 5.005_03-10
BuildRequires:	perl-TimeDate
%requires_eq	perl
Requires:	%{perl_sitearch}
Requires:	perl-TimeDate
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
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/src/examples/%{name}-%{version}

make install DESTDIR=$RPM_BUILD_ROOT

install examples/* $RPM_BUILD_ROOT/usr/src/examples/%{name}-%{version}

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Metadata
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {Changes,README}.gz

%{perl_sitelib}/Metadata
%{perl_sitearch}/auto/Metadata

%{_mandir}/man3/*

/usr/src/examples/%{name}-%{version}
