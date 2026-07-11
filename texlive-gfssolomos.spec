%global tl_name gfssolomos
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	A Greek-alphabet font
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/greek/gfs/gfssolomos
License:	ofl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/gfssolomos.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/gfssolomos.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Solomos is a font which traces its descent from a calligraphically-
inspired font of the mid-19th century. LaTeX support, for use with the
LGR encoding only, is provided.

