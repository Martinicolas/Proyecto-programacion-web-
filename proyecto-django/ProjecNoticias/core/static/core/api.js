

const news = fetch("http://newsapi.org/v2/everything?q=futbol&sortBy=publishedAtA&language=es&pageSize=10&apiKey=44c17e645d384685a160b3171d7b75a8")
    .then(res => res.json())
    .then(data => {
        const noticiasCnt = document.querySelector(".noticias");

        for (const item of data.articles) {
            noticiasCnt.innerHTML += `
            <div class="noticias_item">
                <div class="card col-12">
                    <img src="${item.urlToImage}"/>
                    <div class="card-body">
                        <h1>${item.title}</h1>
                        <p>${item.content}</p>
                    </div>
                </div>
            </div>
        `;
        }






    });