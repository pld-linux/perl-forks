#
# Conditional build:
%bcond_with	tests	# perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	forks
%define		pnam	forks
Summary(pl.UTF-8):	drop-in replacement for Perl threads using fork()
Name:		perl-forks
Version:	0.34
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://search.cpan.org/CPAN/authors/id/R/RY/RYBSKEJ/%{pnam}-%{version}.tar.gz
# Source0-md5:	26e5b395cb24975f9b99414fe1d748f1
URL:		http://search.cpan.org/dist/forks/
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The "forks" pragma allows a developer to use threads without having to have a threaded perl.

%prep
%setup -q -n %{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{perl_vendorlib}/forks

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorarch}/forks.pm
%dir %{perl_vendorarch}/auto/forks
%attr(755,root,root) %{perl_vendorarch}/auto/forks/*.so
%{perl_vendorarch}/forks
%{perl_vendorarch}/threads
%{_mandir}/man3/*
