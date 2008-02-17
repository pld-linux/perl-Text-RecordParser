#
# Conditional build:
%bcond_with	tests		# perform "make test"
				# Text::TabularDisplay 1.21 not available yet
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Text
%define	pnam	RecordParser
Summary:	Text::RecordParser - read record-oriented files
Summary(pl.UTF-8):	Text::RecordParser - odczyt plików rekordowych
Name:		perl-Text-RecordParser
Version:	1.2.1
Release:	3
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Text/%{pdir}-%{pnam}-v%{version}.tar.gz
# Source0-md5:	65c2a85a2ed2a9bc791d377954bd5a44
URL:		http://search.cpan.org/dist/Text-RecordParser/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Text-TabularDisplay >= 1.21
BuildConflicts:	perl-Text-TabularDisplay = 1.20
%endif
# sigh... perl.prov can't handle version->new(...) -- Safe.pm
Provides:	perl(Text::RecordParser) = %{version}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq	'perl(Text::RecordParser)'

%description
This module is for reading record-oriented data. The most common
example have records separated by newlines and fields separated by
commas or tabs, but this module aims to provide a consistent interface
for handling sequential records in a file however they may be
delimited. Typically this data lists the fields in the first line of
the file, in which case you should call bind_header to bind the field
name. If the first line contains data, you can still bind your own
field names via bind_fields. Either way, you can then use many methods
to get at the data as arrays or hashes.

%description -l pl.UTF-8
Ten moduł służy do czytania danych zorientowanych rekordowo.
Najpopularniejszy przykład to rekordy oddzielone nowymi liniami i pola
oddzielone przecinkami lub tabulatorami, ale celem tego modułu jest
dostarczenie spójnego interfejsu do obsługi sekwencyjnych rekordów w
pliku niezależnie od sposobu ich rozdzielenia. Typowo dane te
określają pola w pierwszej linii pliku - w tym przypadku należy
wywołać bind_header aby podpiąć nazwy pól. Jeśli pierwsza linia
zawiera dane, nadal można podpiąć własne nazwy pól poprzez
bind_fields. W każdym przypadku można potem używać wielu metod
pobierania danych jako tablice lub hasze.

%prep
%setup -q -n %{pdir}-%{pnam}-v%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes INSTALL TODO
%attr(755,root,root) %{_bindir}/*
%{perl_vendorlib}/Text/*.pm
%{perl_vendorlib}/Text/RecordParser
%{_mandir}/man?/*
