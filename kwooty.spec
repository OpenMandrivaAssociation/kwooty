%define		major	0
%define		libname	%mklibname %{name}core %{major}

Name:		kwooty
Version:	0.8.0
Release:	1
Summary:	A friendly NZB Usenet binary downloader
License:	GPLv2+
Group:		Networking/News
URL:		http://kwooty.sourceforge.net/
Source0:	%{name}-%{version}.tar.gz
BuildRequires:	cmake >= 2.6.0
BuildRequires:	kdebase4-workspace-devel >= 4.6.0
BuildRequires:	kdelibs4-devel >= 4.6.0
BuildRequires:	gettext
#BuildRequires:	msgfmt
BuildRequires:	desktop-file-utils
Requires:	parchive2
Requires:	unrar
Requires:	%{libname} = %{version}

%description
A friendly NZB newsgroup binary grabber. Its main features are:
- Automatic files verifying/repairing (par2 program required)
- Automatic archive extraction (unrar program required)
- Multi-server support
- Direct file downloading after opening a .nzb file
- Save/Restore pending downloads when application is closed/open
- System shutdown scheduling
- File queue and priority management
- SSL connection support
- Pause/Resume downloads.


%package -n %{libname}
Summary:		Librery for Kwoot usenet binary grabber
Group:		System/Libraries

%description -n %{libname}
Main library for Kwooty.


%prep
%setup -q
# The build directory already exist:
# removing to avoid errors later from our build scripts
rmdir build

# Remove wrong file perms
chmod -x COPYING
chmod -x README.txt


%build
%cmake
%make


%install
rm -rf %{buildroot}
# The makefile assumes we are in the build directory
cd build
%makeinstall_std

# Remove an unwanted category
desktop-file-install  \
		    --remove-category=Internet \
		    --dir %{buildroot}%{_kde_datadir}/applications/kde4 ../src/%{name}.desktop


%find_lang %{name}


%files -f build/%{name}.lang
%doc COPYING README.txt TODO
%{_kde_appsdir}/%{name}/*
%{_kde_bindir}/%{name}
%{_kde_libdir}/kde4/%{name}_*.so
%{_kde_iconsdir}/hicolor/*/apps/%{name}.png
%{_kde_applicationsdir}/%{name}.desktop
%{_kde_services}/%{name}_*.desktop
%{_kde_servicetypes}/%{name}*.desktop
%{_kde_datadir}/config.kcfg/%{name}*.kcfg

%files -n %{libname}
%doc COPYING
%{_kde_libdir}/lib%{name}core.so*
