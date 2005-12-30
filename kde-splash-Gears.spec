%define		_splash		Gears

Summary:	KDE splash screens
Summary(pl):	Ekrany startowe KDE
Name:		kde-splash-%{_splash}
Version:	1.0
Release:	1
License:	GPL
Group:		X11/Amusements
# source files were repackaged into one tar because builder wasn't
# able to correctly handle spaces in original filenames
Source0:	%{name}.tar.gz
# NoSource0-md5:	1f175c9f50e58d8831ea279d4d493130
NoSource:	0
URL:		http://www.kde-look.org/content/show.php?content=30999
Provides:	kde-splash
Requires:	kdebase-desktop >= 9:3.2.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Collection of simple but nice splash screens with KDE Gears. Contains
seven different versions.

%description -l pl
Kolekcja prostych, ale ³adnych ekranów startowych z "zêbatkami KDE".
Zawiera siedem ró¿nych wersji.

%prep
%setup -q -c %{_splash} -n %{_splash}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/apps/ksplash/Themes/%{_splash}\ -\ {alu,blue,green,ice,oil,plastic,rusty}\ edition
install %{_splash}\ -\ alu\ edition/* $RPM_BUILD_ROOT%{_datadir}/apps/ksplash/Themes/%{_splash}\ -\ alu\ edition
install %{_splash}\ -\ blue\ edition/* $RPM_BUILD_ROOT%{_datadir}/apps/ksplash/Themes/%{_splash}\ -\ blue\ edition
install %{_splash}\ -\ green\ edition/* $RPM_BUILD_ROOT%{_datadir}/apps/ksplash/Themes/%{_splash}\ -\ green\ edition
install %{_splash}\ -\ ice\ edition/* $RPM_BUILD_ROOT%{_datadir}/apps/ksplash/Themes/%{_splash}\ -\ ice\ edition
install %{_splash}\ -\ oil\ edition/* $RPM_BUILD_ROOT%{_datadir}/apps/ksplash/Themes/%{_splash}\ -\ oil\ edition
install %{_splash}\ -\ plastic\ edition/* $RPM_BUILD_ROOT%{_datadir}/apps/ksplash/Themes/%{_splash}\ -\ plastic\ edition
install %{_splash}\ -\ rusty\ edition/* $RPM_BUILD_ROOT%{_datadir}/apps/ksplash/Themes/%{_splash}\ -\ rusty\ edition

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/apps/ksplash/Themes/*
