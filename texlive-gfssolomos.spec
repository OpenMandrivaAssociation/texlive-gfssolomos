%global tl_name gfssolomos
%global tl_revision 79618
%global tl_version 1.0

Name:		texlive-%{tl_name}
Epoch:		1
Version:	%{tl_version}
Release:	%{tl_revision}.1
Summary:	A Greek-alphabet font
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/greek/gfs/gfssolomos
License:	ofl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/gfssolomos.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/gfssolomos.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{version}

%description
Solomos is a font which traces its descent from a calligraphically-
inspired font of the mid-19th century. LaTeX support, for use with the
LGR encoding only, is provided.


%install -a
mkdir -p %{buildroot}%{_texmf_updmap_d}
cat > %{buildroot}%{_texmf_updmap_d}/%{tl_name} <<'TL_DROPIN_EOF'
# from gfssolomos:
Map gfssolomos.map
TL_DROPIN_EOF
