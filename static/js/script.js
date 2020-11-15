// var insertHtml = function (selector, html) {
//   var targetElem = document.querySelector(selector);
//   targetElem.innerHTML = html;
// };

// var showLoading = function(selector) {
// 	var html = "<div class='text-center'>";
// 	html += "<img src='./images/ajaxloader.gif'></div>";
// 	insertHtml(selector, html);
// };

document.addEventListener("DOMContentLoaded",function(event){

	// scroll
	if(IntersectionObserver){

		let callback = function(entries){
			entries.forEach(entry => {
				if(entry.isIntersecting && !entry.target.classList.contains('animated')){
					entry.target.classList.add('animated');
				}
			});
		}

		let observer = new IntersectionObserver(callback, {
			root : null,
			threshold : 0.3
		});

		let items = document.querySelectorAll('.scrolleffect');
		items.forEach((item) => {
			item.classList.add('animation');
			observer.observe(item);
		});
	}



    // typewriter effect
	const array = ['Faculty.', 'Mates.', 'Seniors.'];

	function typeWriter(textele, i, fnCallback){

		if(i < textele.length){

			document.querySelector("#main").querySelector("#typeeffect").querySelector("span").innerHTML = textele.substring(0, i+1);

			setTimeout(function() {
	            typeWriter(textele, i+1, fnCallback)
	        }, 200);
		}
		else{
			setTimeout(fnCallback, 900)
		}
	}
	
    function startAnimation(i){
    	if (typeof array[i] == 'undefined'){
	        setTimeout(function() {
	          startAnimation(0);
	        }, 1000);
	     }

    	if(array[i] != 'undefined'){
    		typeWriter(array[i], 0, function(){
    			startAnimation(i+1);
    		});
    	}
    }

	startAnimation(0);

});





