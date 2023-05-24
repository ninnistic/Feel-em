<template>
<div class="container">
		<div id="mainTopCarousel" class="carousel slide" data-bs-ride="carousel" style="width:2000px; height:700px;">
		<div class="carousel-inner">
			<div class="carousel-item active">
				<div class="main-top-promotion">
					<video class="main-top-promotion-video" style="width:2000px; height:700px;" autoplay="autoplay" loop="loop" muted="muted">
						<source src="@/assets/movie/movie.mp4" type="video/mp4">
					</video>
					<div class="container">
						<div class="row align-items-center" style="width:800px; height:700px;">
							<div class="col-sm-12 col-md-6 text-md-start">
								<div class="py-3 py-md-5">
									<h1 class="text-white display-1 movie-title">DUNE</h1><br>
									<h2 class="text-white movie-description">
										바람과 모래로 쓴 <br>대서사시의 서문
									</h2><br>
									<p class="text-white">두려워하지 말라, 두려움은 정신을 죽이고, <br>세계를 소멸시키는 작은 죽음이다</p>
									<p class="text-white mb-4 fs-5" id="shortcut">
										바로 가기 >									
									</p>
								</div>
							</div>
						</div>
					</div>
				</div>
			</div>
			<div class="carousel-item">
				<div class="main-top-promotion">
					<video class="main-top-promotion-video" style="width:2000px; height:700px;" autoplay="autoplay" loop="loop" muted="muted">
						<source src="@/assets/movie/movie2.mp4" type="video/mp4">
					</video>
					<div class="container">
						<div class="row align-items-center" style="width:800px; height:700px;">
							<div class="col-sm-12 col-md-6 text-md-start">
								<div class="py-3 py-md-5">
									<h1 class="text-white display-1 movie-title">
										FAST-X
									</h1><br>
									<h2 class="text-white movie-description">
										달리거나, 죽거나.
									</h2><br>
									<p class="text-white">죽은놈이 살아 돌아온 이유는 딱 하나지. 복수</p>
									<p class="text mb-4 fs-5" id="shortcut">
										바로가기 >
									</p>
								</div>
							</div>
						</div>
					</div>
				</div>
			</div>
		</div>
		<button class="carousel-control-prev" type="button" data-bs-target="#mainTopCarousel" data-bs-slide="prev">
			<span class="carousel-control-prev-icon" aria-hidden="true"></span>
			<span class="visually-hidden">Previous</span>
		</button>
		<button class="carousel-control-next" type="button" data-bs-target="#mainTopCarousel" data-bs-slide="next">
			<span class="carousel-control-next-icon" aria-hidden="true"></span>
			<span class="visually-hidden">Next</span>
		</button>
	</div>
	</div>
</template>
<script>


export default {
	name: 'VideoCard',
}
</script>

<style scoped>
#mainTopCarousel{
	width: 100%;
}
.main-top-promotion {
  display:flex;
	justify-content: center;
  width: 100%;
	align-self: center;
}
.container {
  display:flex;
	justify-content: center;
	align-self: center;
}

.main-top-promotion-video {
  height: 100%;
  width: 100%;
  margin: 0px;
  padding: 0px;
  position: absolute;
  left: 0;
  top: 0;
  object-fit: cover;
	width: 100%;
}

.main-top-promotion > .container {
  position: relative;
	width: 100%;
	right:280px;
}

.carousel-control-next, .carousel-control-prev {
  width: 7% !important;

}

.movie-title {
	font-size : 6em;
	font-weight: 600;
}

.movie-description{
	font-size : 2em;
	font-weight: 200;
}
.movie-sub-description{
	font-size : 3em;
	font-weight: 400;
}
#shortcut {
	color : #627278;
	font-weight: 500;
}

#shortcut:hover{
	color : white;
	cursor : pointer;
}
</style>
