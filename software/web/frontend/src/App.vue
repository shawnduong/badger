<!-- Template -->

<template>

<router-view />

</template>

<!-- Style -->

<style>

:root {
	--dark   : #575757;
	--medium : #9A9A9A;
	--light  : #D9D9D9;
	--white  : #FFFFFF;
	--black  : #000000;
}

@font-face {
	font-family: "Montserrat";
	src: url("@/assets/fonts/Montserrat/Montserrat-Regular.ttf");
}

html {
	background-color: var(--dark);
	color: var(--white);
	font-family: "Montserrat";
}

body {
	margin: 0;
}

h1 {
	font-size: 64px;
	font-weight: 400;
	margin-bottom: 0.1em;
}

h2 {
	font-size: 20px;
	font-weight: 200;
	margin-bottom: 0.1em;
}

.proceed {
	content: url("@/assets/svg/proceed.svg");
	height: 32px;
	vertical-align: middle;
	cursor: pointer;
}

</style>
