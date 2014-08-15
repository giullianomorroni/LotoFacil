<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>LEasy</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="site com dados sobre a loto fácil">
    <meta name="author" content="Giulliano Morroni">
	<link id="callCss" rel="stylesheet" href="/static/css/bootstrap.min.css" type="text/css" media="screen" charset="utf-8" />

	<link id="callCss"rel="stylesheet" href="/static/css/style.css" type="text/css" media="screen" charset="utf-8" />
	<link href="/static/css/bootstrap-responsive.min.css" rel="stylesheet">
    <link href='http://fonts.googleapis.com/css?family=Coming+Soon' rel='stylesheet' type='text/css'>
</head>

<body>
<div id="headerSection">
    <div class="container-fluid">
        <div class="span3 logo">
            <h2>Loto Fácil</h2>
            <a href="#">
            <img src="/static/img/logo1.png" alt="" /></a>
        </div>
    
        <div class="navbar">
            <div class="nav-collapse">
                <ul class="nav">
                    <li><a href="#ourServices" id="estouComSorteLink">Estou com sorte</a></li>
                    <li><a href="#portfolioSection">O Melhor Jogo</a></li>
                    <li><a href="#blogSection">Compartilhe</a></li>
                    <li><a href="#recentpostSection">Analisador</a></li>
                    <li><a href="#meetourteamSection">Desenvolvedores</a></li>
                </ul>
            </div>
        
            <button type="button" class="btn btn-navbar" data-toggle="collapse" data-target=".nav-collapse">
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
            </button>
        </div>
    </div>
</div>

    

<div id="carouselSection" class="cntr"> 
        <div id="myCarousel" class="carousel slide">
        
            <div class="carousel-inner">
                <div class="item active">
                    <a class="cntr" href="#"><img src="/static/img/crr1.jpg" alt=""></a>
                </div>
                <div class="item">
                    <a class="cntr" href="#"><img src="/static/img/crr1.jpg" alt=""></a>
                </div>
              </div>
            <a class="carousel-control left" href="#myCarousel" data-slide="prev">&lsaquo;</a>
            <a class="carousel-control right" href="#myCarousel" data-slide="next">&rsaquo;</a>
        </div>
</div>



<!-- Estou com sorte ======================================== -->
<div id="ourServices">  
	<div class="container"> 
		<div class="row">
			<div class="row-fluid">
				<div class="span12">
                    <h3 style="font-family: 'Coming Soon', cursive;">
                     para que o nosso livre arbítrio não seja extinto, 
                     julgo poder ser verdade que a SORTE seja o árbitro da 
                     metade das nossas ações, mas que ainda nos deixe governar 
                     a outra metade, ou quase. 
                    </h3>
                     <h4>"Nicolau Maquiavel"</h4>
                    <span id="luckNumbers">  </span>
                    <span id="luckPercent">  </span>
					</div>
				</div>
			</div>
		</div>
	</div>	
</div>




<!-- O Melhor Jogo======================================== -->
<div id="portfolioSection">
    <div class="span6" style="width:100%">
        <h1 class="cntr">O Melhor Jogo</h1>
        <p>Como você prefere que seu jogo seja montado ? Aqui é a pastelaria do bons números, é só pedir. </p>
    </div>
    <div class="container"> 
        <div class="clr"></div>
        <div class="tabbable tabs">
            <div class="tab-content label-primary">
                <div class="tab-pane active" id="all">
                    <ul class="thumbnails">
                        <li class="span4">
                            <div>
                                <h3> As melhores repetições </h3>
                                <button onclick="order('melhores_repeticoes');" >aqui</button>
                            </div>
                        </li>
                        <li class="span4">
                            <div>
                                <h3>As melhores colunas</h3>
								<button onclick="order('melhores_colunas');" >aqui</button>
                            </div>
                        </li>
                        <li class="span4">
                            <div>
                                <h3>Com percentual de acerto</h3>
								<button onclick="order('percentual');" >aqui</button>
                            </div>
                        </li>
                        <li class="span4">
                            <div>
                                <h3>Complete meu jogo</h3>
								<button onclick="order('complete');" >aqui</button>
                            </div>
                        </li>
                        <li class="span4">
                            <div>
                                <h3>Números aletórios</h3>
								<button onclick="order('randomico');" >aqui</button>
                            </div>
                        </li>
                    </ul>
                    <span id="orderNumbers">  </span>
                    <span id="orderPercent">  </span>
                </div>
            </div>
        </div>
    </div>
</div>





<!-- Compartilhe seus jogos -->
<div id="blogSection">
    <div class="container">
        <div class="row span12"> 
            <div class="span8">
                <div class="inner">
                    <h1>Contribua com sua experiência, não custa nada</h1>
                    <p>
                    Nós queremos saber você já conseguiu bons resultados com nossos números.
                    E de quanto aproximadamente foi seu lucro, ou então se você não teve lucro algum.
                    </p>
                    <h4>se você ganhou: </h4>
                    <a href="#" class="btn btn-large btn-success">até 5,00</a>
                    <a href="#" class="btn btn-large btn-success">até 15,00</a>
                    <a href="#" class="btn btn-large btn-success">até 50,00</a>
                    <a href="#" class="btn btn-large btn-success">até 1.000,00</a>
                    <a href="#" class="btn btn-large btn-success">mais 1.000,00</a>
                </div>

                <div class="inner">
                    <h4>se você não ganhou: </h4>
                    <a href="#" class="btn btn-large btn-danger">nunca ganhei</a>
                    <a href="#" class="btn btn-large btn-danger">dessa vez não deu</a>
                </div>

            </div>
        
            <div class="span4">
                <img src="/static/img/img-10.png" alt="" />
            </div>
        </div>
        
        <hr class="soften clear"/>
        
        <div class="row span12">
            <div class="span4">
                <img src="/static/img/img-10.png" alt="" />
            </div>
            <div class="span8">
                <div class="inner">
                    <h1>Layered Neatly Photoshop Template</h1>
                    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed et quam est. Mauris faucibus tellus ac auctor posuere. Integer lobortis purus a felis adipiscing, eget ornare justo semper. Etiam commodo tincidunt ante.</p>
                    <a href="#" class="btn btn-large btn-primary">SHOW MORE</a>
                </div>
            </div>    
        </div>
    </div>
</div>





<!-- Analisador======================================== -->
<div id="recentpostSection">
    <div class="span6">
        <h1 class="cntr">Análise seus números</h1>
        <p>Este site não possui os números da loto fácil, é um espaço voltado a estudos de probabilidade e estatística. 
        Ainda que seu jogo seja avaliado como, pouco provável, você não deve dar 100% de razão à nossa análise, pois ainda assim
        ele pode ser sorteado. Jogos de azar não seguem um padrão comportamental e nem são lógicos, tudo pode acontecer.
        </p>
    </div>
    
    <div class="container"> 
        <div class="tabbable tabs">
            <div class="tab-content label-primary">
                <div class="tab-pane active" id="all">
                    <ul class="thumbnails">
                        
                        <li class="span4">
                            <div class="thumbnail">
                                <div class="blockDtl">
                                <a href="#" ><img src="/static/img/img-12.png" alt=""></a>
                                <h4>Análise Completa</h4>
                                <h6>Base Completa</h6>
                                <p>
                                    Esta análise é feita usando todos os resultados já sorteados pela loto fácil, e comparando eles
                                    aos seus números. Individualmente todos os números foram sorteados uma quantidade de vezes muito próxima. 
                                    Vamos quebrar seu jogo em partes e analisa-lo com nossos algoritmos.
                                </p>
                                
                                </div>
                            </div>
                        </li>
                        <li class="span4">
                            <div class="thumbnail">
                                <div class="blockDtl">
                                    <a href="#"><img src="/static/img/img-12.png" alt=""></a>
                                    <h4>Análise por Tempo</h4>
                                    <h6>Defina o período</h6>
                                    <p>
                                        Esta análise é idêntica à análise completa porém permite especificar
                                        um período, ao invés de utilizar toda a base de dados. Isso permite que seu jogo 
                                        seja avaliado, por exemplo, somente com o mês atual ou com um ano específico.
                                    </p>
                                </div>
                            </div>
                        </li>
                        <li class="span4">
                            <div class="thumbnail">
                                <div class="blockDtl">
                                <a href="#"><img src="/static/img/img-12.png" alt=""></a>
                                <h4>Really Interesting Post</h4>
                                <h6>October 27</h6>
                                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed et quam est. </p>
                               
                                </div>
                            </div>
                        </li>
                    </ul>
                    <form class="form-horizontal" role="form" action="/analisar" method="post">
                        <div class="form-group">
                            <input type="text" class="form-control" pattern="[1-9]*" id="mynumbers" placeholder="Digite aqui seu jogo">
                        </div>
                        <div class="form-group">
                            <button type="submit" class="btn btn-large btn-primary disabled">ANALISAR</button>
                        </div>    
                    </form>
                </div>
            </div>
        </div>
    </div>
</div>





<!-- developers======================================== -->
<div id="meetourteamSection">
    <div class="span6">
        <h1 class="cntr">Developers</h1>
        <p>O site pertence a nós, o conteúdo é para todos. E não se esqueça, se ganhar, e você vai ganhar, a gente aceita um agrado </p>
     </div>
     
     <div class="container"  style="width:100%;"> 
        <div class="tabbable tabs">
            <div class="tab-content label-primary">
                <div class="tab-pane active" id="all">
                    <ul class="thumbnails">
                        <li class="span4">
                            <div class="thumbnail">
                                <div class="blockDtl">
                                    <a href="#" ><img src="/static/img/img-11.png" alt=""></a>
                                    <h4>Giulliano Morroni</h4>
                                    <h5>Vai morrer pobre</h5>
                                    <p>Escreveu algoritmos baseados em análises de dados passadas para prever o seu futuro. </p>
                                    <a class="facebook" href="#"></a>
                                    <a class="twitter" href="#"></a>
                                    <a class="pin" href="#"></a>
                                </div>
                            </div>
                        </li>
                        <li class="span4">
                            <div class="thumbnail">
                                <div class="blockDtl">
                                <a href="#"><img src="/static/img/img-11.png" alt=""></a>
                                <h4>Pauline Santos</h4>
                                <h5>Futura Milionária</h5>
                                <p>Aposta nos resultados gerados e contribue para melhoria contínua do site. </p>
                                <a class="facebook" href="#"></a>
                                <a class="twitter" href="#"></a>
                                <a class="pin" href="#"></a>
                                </div>
                            </div>
                        </li>
                        <li class="span4">
                            <div class="thumbnail">
                                <div class="blockDtl">
                                <a href="#"><img src="/static/img/img-11.png" alt=""></a>
                                <h4>Macarrão com Salsicha</h4>
                                <h5>Almoço</h5>
                                <p>Contribue com a soma de calorias e saciedade do time. </p>
                                <a class="facebook" href="#"></a>
                                <a class="twitter" href="#"></a>
                                <a class="pin" href="#"></a>
                                </div>
                            </div>
                        </li>
                    </ul>
                </div>
            </div>
        </div>
    </div>
</div>





<!-- Contact Section -->
<div id="contactSection">
    <div class="footerSection container">
        <div class=" span4 socialicon">
            <a class="facebook" href="http://www.facebook.com/"></a>
            <a class="twitter" href="http://www.twitter.com/"></a>
            <a class="html5" href="#"></a>
            <a class="icon2" href="#"></a>
        </div>
        <div class="span8 copyright"><p>  Copyright 2014 | Developed By </a></p></div>
    </div>
</div> 




<a href="#" class="go-top" ><i class="icon-arrow-up"></i></a>

<!-- Javascript
    ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->

<script src="/static/js/jquery-1.9.1.min.js"></script>
<script src="/static/js/bootstrap.min.js" type="text/javascript"></script>
<script src="/static/js/jquery.scrollTo-1.4.3.1-min.js" type="text/javascript"></script>
<script src="/static/js/jquery.easing-1.3.min.js"></script>
<script src="/static/js/default.js"></script>
<script src="/static/js/main.js"></script>

<script type="text/javascript">

	$(document).ready(function() {
	$('#myCarousel').carousel({
	  interval: 5000
	});
	
	});
 
</script>

</body>
</html>
