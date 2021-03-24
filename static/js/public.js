$(document).ready(function(){
    $('#myTable').DataTable();
    $('#myTable1').DataTable();
    $('.dataTables_info').remove();

    $('.min-qty').click(function(){
    	var id = $(this).attr('data-id');
    	var qty = parseInt($('#nilai-qty-' + id).text());
    	var harga = parseInt($('#harga-' + id).attr('data-harga'));
    	console.log(harga);
    	if(qty > 0){
    		qty--;
    		harga *= qty;
    		var coin = harga > 0 ? numeral(harga).format('0,0'): 0;
    		$('#harga-' + id).text('Rp. ' + coin);
    		$('#nilai-qty-' + id).text(qty);
    		$('#stok-qty-' + id).val(qty);
    	}
    });

    $('.plus-qty').click(function(){
    	var id = $(this).attr('data-id');
    	var qty = parseInt($('#nilai-qty-' + id).text());
    	var harga = parseInt($('#harga-' + id).attr('data-harga'));
    	console.log(harga);
    	qty++;
    	harga *= qty;
    	var coin = harga > 0 ? numeral(harga).format('0,0'): 0;
    	$('#harga-' + id).text('Rp. ' + coin);
    	$('#nilai-qty-' + id).text(qty);
    	$('#stok-qty-' + id).val(qty);
    });
});