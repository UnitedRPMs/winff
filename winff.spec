%global gitdate 20170603
%global commit0 0b85024d5aac56c04f0cb53f37b92780dc4791a4
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global gver .git%{shortcommit0}

Name:		winff
Summary:	Graphical video and audio batch converter using ffmpeg
Version:	1.5.5
Release:	2%{?dist}
URL:		http://winff.org/
Source0:	https://github.com/WinFF/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz
Source1:	winff.desktop
License:	GPLv3
Group:		Applications/Multimedia

Requires:	ffmpeg
Requires:	hicolor-icon-theme
BuildRequires:	dos2unix
BuildRequires:	fpc
BuildRequires:	fpc-src
BuildRequires:	glib2-devel
BuildRequires:	gtk2-devel
BuildRequires:	lazarus
BuildRequires:	libX11-devel
BuildRequires:	desktop-file-utils
BuildRequires:	fdupes
BuildRequires:	gettext
Conflicts:	winff-qt
BuildRoot:	%{_tmppath}/%{name}-%{version}-build

%description
WinFF is a GUI for the command line video converter FFMPEG.
It will convert most any video file that FFmpeg will convert.
WinFF does multiple files in multiple formats at one time.
You can for example convert mpeg, flv, and mov
all into avi all at once.

%prep
%autosetup -n %{name}-%{commit0} 
cd winff
dos2unix *.txt
chmod 644 *.txt docs/*.pdf docs/*.odg docs/*.odt docs/*.txt winff-icons/*.txt

%build
cd winff
lazbuild \
	--lazarusdir=%{_libdir}/lazarus \
%ifarch x86_64
	--cpu=x86_64 \
%endif
	--widgetset=gtk2 \
	-B winff.lpr


%install 
cd winff
install -dm 755 %{buildroot}/%{_bindir}
install -dm 755 %{buildroot}/%{_mandir}/man1
install -dm 755 %{buildroot}/%{_datadir}/winff/languages/
install -dm 755 %{buildroot}/%{_datadir}/applications/

install -m 644 %{SOURCE1} %{buildroot}/%{_datadir}/applications/
install -m 644 presets.xml %{buildroot}/%{_datadir}/winff/
install -m 644 languages/*.po %{buildroot}/%{_datadir}/winff/languages/
install -m644 winff.1 %{buildroot}/%{_mandir}/man1
install -m644 winff %{buildroot}/%{_bindir}/
chmod a+x %{buildroot}/%{_bindir}/winff

install -dm 755 %{buildroot}/%{_datadir}/icons/hicolor
for i in 16 24 32 48; do
  install -dm 755 %{buildroot}/%{_datadir}/icons/hicolor/"$i"x"$i"/apps
  install -m 644 winff-icons/"$i"x"$i"/*.png %{buildroot}/%{_datadir}/icons/hicolor/"$i"x"$i"/apps
done


%clean
rm -rf %{buildroot}/

%files 
%defattr(755, root, root) 
%{_bindir}/winff
%{_datadir}/winff/
%{_datadir}/applications/winff.desktop
%{_datadir}/icons/*
%{_mandir}/man1/*



%changelog

* Thu Jun 15 2017 David Vásquez <davidjeremias82 AT gmail DOT com> - 1.5.5-2.git0b85024
- Changed group

* Sat Jun 03 2017 David Vásquez <davidjeremias82 AT gmail DOT com> - 1.5.5-1.git0b85024
- Updated to 1.5.5-1.git0b85024

* Thu Jan 07 2016 David Vásquez <davidjeremias82 AT gmail DOT com> - 1.5.4-1-git86c3560
- Updated to 1.5.4-1-git86c3560

* Fri Mar 20 2015 David Vásquez <davidjeremias82 AT gmail DOT com> - 1.5.3-1
- Updated to 1.5.3

*Tue Mar 04 2014 David Vásquez <davidjeremias82 AT gmail DOT com> - 1.5.2-2
- Changed path
- Use now ffmpeg-full

* Mon Oct 07 2013 David Vasquez <davidjeremias82 AT gmail DOT com> 1.5.2-1
- Update to vesion 1.5.2

* Sat May 18 2013 David Vásquez <davidjeremias82 AT gmail DOT com> - 1.5.0-1
- Rebuild for Fedora 18
- Includes new dependencies
- Update presets
- Initial build

