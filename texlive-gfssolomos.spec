Name:		texlive-gfssolomos
Version:	18651
Release:	2
Summary:	A Greek-alphabet font
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/greek/gfs/gfssolomos
License:	OFL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gfssolomos.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gfssolomos.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Solomos is a font which traces its descent from a
calligraphically-inspired font of the mid-19th century. LaTeX
support, for use with the LGR encoding only, is provided.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/afm/public/gfssolomos/GFSSolomos-Regular.afm
%{_texmfdistdir}/fonts/enc/dvips/gfssolomos/gpsolomos.enc
%{_texmfdistdir}/fonts/map/dvips/gfssolomos/gfssolomos.map
%{_texmfdistdir}/fonts/opentype/public/gfssolomos/GFSSolomos.otf
%{_texmfdistdir}/fonts/tfm/public/gfssolomos/gsolomos8a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfssolomos/gsolomos8r.tfm
%{_texmfdistdir}/fonts/type1/public/gfssolomos/GFSSolomos-Regular.pfb
%{_texmfdistdir}/fonts/vf/public/gfssolomos/gsolomos8a.vf
%{_texmfdistdir}/tex/latex/gfssolomos/gfssolomos.sty
%{_texmfdistdir}/tex/latex/gfssolomos/lgrsolomos.fd
%doc %{_texmfdistdir}/doc/fonts/gfssolomos/OFL-FAQ.txt
%doc %{_texmfdistdir}/doc/fonts/gfssolomos/OFL.txt
%doc %{_texmfdistdir}/doc/fonts/gfssolomos/README
%doc %{_texmfdistdir}/doc/fonts/gfssolomos/gfssolomos.pdf
%doc %{_texmfdistdir}/doc/fonts/gfssolomos/gfssolomos.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}
