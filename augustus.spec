Name:           augustus
Version:        3.0.1
Release:        1
Summary:        An open source re-implementation of Caesar III
License:        MIT
Group:          Games/Other
Url:            https://github.com/Keriew/augustus
Source0:	https://github.com/Keriew/augustus/archive/refs/tags/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  pkgconfig(sdl2)
BuildRequires:	pkgconfig(SDL2_mixer) 
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(expat)

%description
Augustus is an open source re-implementation of Caesar III.
Augustus is a fork of the Julius project that intends to incorporate gameplay changes.
The aim of this project is to provide enhanced, customizable gameplay to Caesar 3 using project Julius UI enhancements.

Augustus is able to load Caesar 3 and Julius saves, however saves made with Augustus will not work outside Augustus.

Gameplay enhancements include:
Roadblocks
Market special orders
Global labour pool
Partial warehouse storage
Increased game limits
Zoom controls
And more!

Because of gameplay changes and additions, save files from Augustus are NOT compatible with Caesar 3 or Julius. 
Augustus is able to load Caesar 3 save files, but not the other way around. 
If you want vanilla experience with visual and UI improvements, or want to use save files in base Caesar 3, check Julius.

Augustus, like Julius, requires the original assets (graphics, sounds, etc) from Caesar 3 to run. 
Augustus optionally supports the high-quality MP3 files once provided on the Sierra website.

#---------------------------------------------------------

%prep
%autosetup -p1

%build
%cmake
%make_build

%install
%make_install -C build

%files
%{_bindir}/%{name}
%{_datadir}/applications/com.github.keriew.augustus.desktop
%{_datadir}/augustus-game/assets/
%{_datadir}/icons/hicolor/*/apps/com.github.keriew.augustus.png
%{_datadir}/metainfo/com.github.keriew.augustus.metainfo.xml
