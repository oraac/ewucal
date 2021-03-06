
//
//
// Runs the dynamic part of the website for image
// This Find offsets also performs the task of validating them
//
////////////////////////////////////////////////////


function iWindow (iImg) {
    var settings = {
        window_width: screen.availWidth - 40,
        window_height: screen.availHeight - 250,
        window_ratio: (screen.availWidth - 40) / (screen.availHeight - 250),
        zoom_max: 20, // 100X initial zoom
    };

    var $image = $('.draggable').extend({
        boxes: null,        //These are for the actual uploading
        to_do_id: iImg.toDoId,
        min_width: null,
        max_width: null,
        lw_ratio: null,
        scale_factor: null,
        zoom_factor: null,
        offset_left: null,
        position_left: null,
        middle_x: null,
        middle_y: null,
        page_id: iImg.pageId,
        src_length: iImg.height,
        src_width: iImg.width,
        update_boxes: true,
        update_box_visibility: true,
        modified: false,
        box_last_selected: null,
        box_first: null,
        box_is_selected: false,
        all_boxes_reviewed: false,
        draw_new_box_mode: false,
        x_start: null,
        y_start: null,
    });

    
    $image.lw_ratio = $image.src_length / $image.src_width;
    $image.min_width = settings.window_width * 0.3;
    $image.width = $image.min_width;
    $image.scale_factor = $image.width / $image.src_width;
    $image.max_width = $image.min_width * settings.zoom_max;
    
    $image.height = $image.min_width * $image.lw_ratio;
    
    $image.attr('src', iImg.URL);
    $image.css({'position': 'absolute',
                'transform-origin': 'left bottom'}).wrap('<div class="page_viewport"></div>');


    var $viewport = $image.parent().resizable().extend({
        hLine: $( '<div class="hLine"></div>' ).hide(),
        vLine: $( '<div class="vLine"></div>' ).hide()
    })
    
    $viewport.append($viewport.hLine).append($viewport.vLine);
    
    function updateCrossHairPos(e) {
        $viewport.hLine.css({top: e.pageY - 14});
        $viewport.vLine.css({left: e.pageX - 14});
    }
    
    $viewport.mousemove(function(e) {
        updateCrossHairPos(e)
    });
    $viewport.extend({
        middle_x: Math.round($viewport.width() / 2),
        middle_y: Math.round($viewport.height() / 2),
        x_start: null,
        y_start: null
    });
    $viewport.css({
        width: settings.window_width,
        height: settings.window_height
    });
    


        $viewport.extend({
        draw_overlay: $('<div class="draw-overlay"></div>').selectable({
            start: function(e){
                $viewport.vLine.hide();
                $viewport.hLine.hide();
                $viewport.x_start = e.pageX;
                $viewport.y_start = e.pageY;
            },
            stop: function(e){
                let p1 = reverseCoordinates({x: Math.min($viewport.x_start, e.pageX) - 14,
                                             y: Math.min($viewport.y_start, e.pageY) - 14
                                        });
                let p2 = reverseCoordinates({x: Math.max($viewport.x_start, e.pageX) - 14,
                                             y: Math.max($viewport.y_start, e.pageY) - 14
                                        });
                $image.box_last_selected = build_a_box({
                    x1: p1.x,
                    x2: p2.x,
                    y1: p1.y,
                    y2: p2.y
                }, true);
                updateCrossHairPos(e);
                $viewport.vLine.show();
                $viewport.hLine.show();
                $image.box_last_selected.selectable.changed = true;
                $image.box_last_selected.selectable.added = true;
                $image.update_boxes = true;
                
                }
        }).hide()
    });
    $viewport.append($viewport.draw_overlay);
    
    var $container = $viewport.parent();
    
    $viewport.boxes = new Set();
    $image.boxes = new Set();
    
    for(i = 0; i < iImg.chars.length; ++i) {
        build_a_box(iImg.chars[i], false);
    }
    $image.offset_left = (175 - $viewport.middle_x) / $image.scale_factor;
    $image.offset_top = (20 - $viewport.middle_y) / $image.scale_factor ;
    var screenupdate = setInterval(updateZoom, 10);
    function updateZoom(){
        if ($image.update_boxes)
        {
            $image.update_boxes = false;
            $image.height = Math.round($image.width * $image.lw_ratio);
            $image.scale_factor = $image.width / $image.src_width;
            $viewport.middle_x = Math.round($viewport.width() / 2);
            $viewport.middle_y = Math.round($viewport.height() / 2);
            
            let im_left = Math.round($image.width * $image.lw_ratio);
            $image.css({
                width: Math.round($image.width),
                height: Math.round($image.width * $image.lw_ratio),
                left: Math.round($image.offset_left * $image.scale_factor + $viewport.middle_x),
                top: Math.round($image.offset_top * $image.scale_factor + $viewport.middle_y)
            });   
            if($image.draw_new_box_mode)
            {
                $viewport.draw_overlay.css({
                    width: Math.round($image.width),
                    height: Math.round($image.width * $image.lw_ratio),
                    left: Math.round($image.offset_left * $image.scale_factor + $viewport.middle_x),
                    top: Math.round($image.offset_top * $image.scale_factor + $viewport.middle_y)
                });
            }
            let i = 0;
            let last_box;
            let all_reviewed = true;
            for (let boxPack of $viewport.boxes)
            {
                if(!boxPack.reviewed)
                {
                    all_reviewed = false;
                }
                if(++i === 1) //Fist
                {
                    $image.box_first = boxPack;
                }
                else
                {
                    if(i === $viewport.boxes.size) //last
                    {
                        boxPack.next_block = $image.box_first;
                        $image.box_first.last_block = boxPack;
                    }
                    last_box.next_block = boxPack;
                    boxPack.last_block = last_box;
                }
                last_box = boxPack;
                boxPack.box_num = i;
                updateBoxPosition(boxPack.selectable);
                updateBoxPosition(boxPack.resizable);
            }
            $image.all_boxes_reviewed = all_reviewed;
        }
    }
    
    function reverseCoordinates(xy) {
        return  {x: Math.round((xy.x - $viewport.middle_x) / $image.scale_factor - $image.offset_left),
                 y: Math.round((xy.y  - $viewport.middle_y) / $image.scale_factor - $image.offset_top)
                };
    }

    
    function updateBoxPosition($box) {
        $box.css({
            left: Math.round($image.scale_factor * ($box.x_top + $image.offset_left) + $viewport.middle_x) - 2,
            top: Math.round($image.scale_factor * ($box.y_top + $image.offset_top) + $viewport.middle_y) - 2,
            width: Math.round($image.scale_factor * $box.x_len) + 2,
            height: Math.round($image.scale_factor * $box.y_len) + 2
        });
    }
    
    
    var $zoom_widget = $('<div class="ui-slider-handle"></div>')
        .slider({
            value: $image.min_width,
            min: $image.min_width,
            max: $image.max_width,
            slide: function (event, ui) {
                $image.update_boxes = true;
                $image.width = ui.value;
            }});
    $container.append($zoom_widget);

    
    $image.draggable({  // Can correct image spazzing out using cursorAt for rotated images.
        drag: function (event, ui) {
            $image.offset_left = (ui.position.left - $viewport.middle_x) / $image.scale_factor;
            $image.offset_top = (ui.position.top - $viewport.middle_y) / $image.scale_factor;
            $image.update_boxes = true;
        },
        scroll: false
    });
    
    $( '.submit_button' ).button().click(function() {
            submit_form(false);
        });
    
    $( '.flag_for_review_button' ).button().click(function() {
        let result = confirm("Are you sure?");
        if(result === true)
        {
            submit_form(true);
        }
    });
    

    
    function submit_form(flagged){
        if(!$image.all_boxes_reviewed && ! flagged)
        {
            alert("review all boxes before submitting: Use TAB / shift TAB to cycle through chars");
            return;
        }
        let deleted_boxes = [];
        let modified_boxes = [];
        let new_boxes = [];
        let modified = false;
        let deleted = false;
        let added = false;
        for (let boxPack of $image.boxes)
        {
            if (boxPack.selectable.changed)
            {
                let $box = boxPack.selectable;
                if($box.deleted)
                {
                    deleted = true;
                    deleted_boxes.push({charId: $box.charId});
                }
                else
                {
                    if($box.added)
                    {
                        added = true;
                        new_boxes.push({ 
                            x_1: $box.x_top,
                            y_1: $box.y_top,
                            x_2: $box.x_len + $box.x_top,
                            y_2: $box.y_len + $box.y_top,
                        });
                    }
                    else
                    {
                        modified = true;
                        modified_boxes.push({
                            charId: $box.charId,
                            x_1: $box.x_top,
                            y_1: $box.y_top,
                            x_2: $box.x_len + $box.x_top,
                            y_2: $box.y_len + $box.y_top,
                        });
                    }
                }
            }
        }
        let message;
        
        message = {to_do_id: $image.to_do_id,
                   flagged_for_review: flagged,
                   deleted_boxes: deleted_boxes,
                   modified_boxes: modified_boxes,
                   new_boxes: new_boxes,
                   page_id: $image.page_id,
                   modified: modified,
                   deleted: deleted,
                   added: added,
                   old_or_new: is_new};
        
        let token = get_csrf_token();

        
        var ajaxcall = $.ajax({
            url: '/ajax/post_characters',
            data: JSON.stringify(message),
            method: 'POST',
            dataType: 'json',
        }).done(function( data ) {
            location.reload();
            }).fail( function(){
                alert("Something went wrong  Call Dave");
            });
    }
    
    
    function update_box_selection(boxPack, recenter){
        boxPack.reviewed = true;
        let $box = boxPack.selectable;
        let $r_box = boxPack.resizable;
        if($image.box_is_selected && !$image.box_last_selected.selectable.deleted)
        {
                $image.box_last_selected.resizable.hide();
                $image.box_last_selected.selectable.show();
        }
        else
        {
            $image.box_is_selected = true;
        }
        $image.box_last_selected = boxPack;
        
        if(recenter) //zoom in and move the window so the box is centered
        {
            $image.offset_left  = (settings.window_width / 2 - $viewport.middle_x) / $image.scale_factor - $box.x_top - $box.y_len / 2;
            $image.offset_top  =  (settings.window_height / 2 - $viewport.middle_y) / $image.scale_factor - $box.y_top - $box.y_len / 2;
           $image.width = settings.window_width / $box.y_len * $image.src_width * 0.3;
           document.title = $image.page_id + " : " + boxPack.box_num + ' / ' + $viewport.boxes.size + " : " + boxPack.selectable.mark;
        }
        
        
        $box.hide();
        $r_box.show();
        $image.update_boxes = true;
        
    }
    
    
    function build_a_box(iChar, reviewed){
        
        var $charBox = $('<div class="char_box"></div>').selectable({
                autoRefresh: false,
                stop: function(event, ui){
                    if(event.shiftKey)
                    {
                        update_box_selection($(this).data('self'), false);
                    }
                    else
                    {
                        update_box_selection($(this).data('self'), true);
                    }
                }}).extend({
                charId : iChar.charId,
                URL : iChar.URL,
                mark : iChar.mark,
                x_top: iChar.x1,
                y_top: iChar.y1,
                x_len: iChar.x2 - iChar.x1,
                y_len: iChar.y2 - iChar.y1,
                x_thumb: iChar.x_thumb,
                y_thumb: iChar.y_thumb,
                selected: false,
                deleted: false,
                changed: false,
                added: false
            }).mouseenter(function(){
                $charBox.toggleClass('char_box', false);
                $charBox.toggleClass('char_box_hover', true);
            }).mouseleave(function(){
                $charBox.toggleClass('char_box_hover', false);
                $charBox.toggleClass('char_box', true);
            });
            
var $dragBox = $('<div class="char_box_resize"></div>').extend({
                charId : iChar.charId,
                x_top: iChar.x1,
                y_top: iChar.y1,
                x_len: iChar.x2 - iChar.x1,
                y_len: iChar.y2 - iChar.y1,
            }).resizable({
                stop: function( event, ui ){
                    $dragBox.x_len = Math.round( ui.size.width / $image.scale_factor);
                    $charBox.x_len = $dragBox.x_len;
                    $dragBox.y_len = Math.round( ui.size.height / $image.scale_factor);
                    $charBox.y_len = $dragBox.y_len;
                    $charBox.changed = true;
                    $image.update_boxes = true;
                }
            }).draggable({
                stop: function( event, ui ){
                    $dragBox.x_top = Math.round( (ui.position.left - $viewport.middle_x) / $image.scale_factor - $image.offset_left );
                    $charBox.x_top = $dragBox.x_top;
                    $dragBox.y_top = Math.round( (ui.position.top - $viewport.middle_y) / $image.scale_factor - $image.offset_top );
                    $charBox.y_top = $dragBox.y_top;
                    $charBox.changed = true;
                    $image.update_boxes = true;
                }
            }).hide();
            
            var boxPack = {selectable:$charBox,
                           resizable:$dragBox,
                           next_box:null,
                           prev_box:null,
                           box_num: null,
                           reviewed: reviewed,
                           just_added: reviewed};

            $charBox.data('self', boxPack);
            $viewport.append($charBox).append($dragBox);
            $viewport.boxes.add(boxPack);
            $image.boxes.add(boxPack);
            
            return boxPack;
    }

////////////////////////////////////////////////////////////////////////////////////////

$(document).keydown(function(event) {
    event.preventDefault();
    const keyName = event.key;

  if (keyName === 'ArrowUp') {
        $image.offset_top += 50 / $image.scale_factor;
        $image.update_boxes = true;
    return;
  }
    if (keyName === 'ArrowDown') {
        $image.offset_top -= 50 / $image.scale_factor;
        $image.update_boxes = true;
    return;
  }
  
    if (keyName === 'ArrowRight') {
        $image.offset_left -= 50 / $image.scale_factor;
        $image.update_boxes = true;
        return;
    }
    if (keyName === 'ArrowLeft') {
        $image.offset_left += 50 / $image.scale_factor;
        $image.update_boxes = true;
    return;
  }
  
    if (keyName === '+') {
        $image.width += $image.width / 10;
        $image.update_boxes = true;
    return;
    }
    
    if (keyName === '-') {
        $image.width -= $image.width / 10;
        $image.update_boxes = true;
    return;
    }
    
   
    if (keyName === 'Insert') {
        if($image.draw_new_box_mode)
        {   $viewport.hLine.hide();
            $viewport.vLine.hide();
            $viewport.draw_overlay.hide();
            $image.draw_new_box_mode = false;
            update_box_selection($image.box_last_selected, false);
        }
        else
        {
            if($image.box_is_selected)
            {
                $image.box_is_selected = false;
                $image.box_last_selected.resizable.hide();
                $image.box_last_selected.selectable.show();
            }
            $viewport.hLine.show();
            $viewport.vLine.show();
            $viewport.draw_overlay.show();
            $image.draw_new_box_mode = true;
            $image.update_boxes = true;
        }
        
        
        return;
    }
    if (keyName === 'Delete') {
        if($image.box_is_selected)
        {
            if ($image.box_last_selected.just_added)
            {
                $image.boxes.delete($image.box_last_selected);
            }
            $image.box_is_selected = false;
            $image.box_last_selected.selectable.deleted = true;
            $image.box_last_selected.selectable.changed = true;
            $image.box_last_selected.resizable.hide();
            $viewport.boxes.delete($image.box_last_selected);
        }
        $image.update_boxes = true;
        return;
    }
    
    if (keyName == 'Tab' || keyName == '*' || keyName == '/') {
        if($image.draw_new_box_mode)
        {
            $viewport.draw_overlay.hide();
            $image.draw_new_box_mode = false;
            update_box_selection($image.box_last_selected, false);
        }
        if($image.box_is_selected)
        {
            if(event.shiftKey || keyName == '/')
            {
                update_box_selection($image.box_last_selected.last_block, true);
            }
            else
            {
                update_box_selection($image.box_last_selected.next_block, true);
            }
        }
        else
        {
            update_box_selection($image.box_first, true);
        }
    }
    
//    console.logconsole.log(`Key pressed ${keyName}`);

	
$viewport.append( $( '<div id="line"></div>' ) )

//Function to draw a vertical line
function draw_vertical_line(width, height, linecolor, xpos, ypos) {
    $('#line').css({'width':width, 'height':height, 'background-color':linecolor, 'left':xpos, 'top':ypos, 'position':'absolute'});
}

draw_vertical_line(1, 100, '#357d35', 50, 10);

});
}
////////////////////////////////////////////////////////////////////////////////////////

var is_new

function startMe( $ ){
    var  $dialog = $( "#dialog" ).dialog({autoOpen: false});
    var  $pages = $.getJSON('/ajax/get_bad_pages').done(iWindow);
}


$(document).ready(startMe);

var element = document.getElementById('box');

var drawLines = function(event) {
  
}
