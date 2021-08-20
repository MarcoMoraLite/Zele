# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request

class especialista():

    def valida_ine(self):
        instanciaCurp = request.env['valida_curp.valida_curp']
        objetoCurp = instanciaCurp.new(ine: ine_binario)
        validar1 = objetoCurp.comprobar2()
        
    def confirma_ine(self):
        instanciaCurp = request.env['valida_curp.valida_curp']
        objetoCurp = instanciaCurp.new(ine: ine_binario)
        validar1 = objetoCurp.confirmarIne()
        
    def valida_cedula(self):
        instanciaCurp = request.env['valida_curp.valida_curp']
        objetoCurp = instanciaCurp.new(ine: ine_binario)
        validar2 = objetoCurp.comprobar()
        
    def confirma_cedula(self):
        instanciaCurp = request.env['valida_curp.valida_curp']
        objetoCurp = instanciaCurp.new(ine: ine_binario)
        validar1 = objetoCurp.confirmarCed()
        
    def valida_foto(self):
        instanciaCurp = request.env['valida_curp.valida_curp']
        objetoCurp = instanciaCurp.new(ine: ine_binario)
        validar3 = objetoCurp.selfie()
        
    def confirma_foto(self):
        instanciaCurp = request.env['valida_curp.valida_curp']
        objetoCurp = instanciaCurp.new(ine: ine_binario)
        validar1 = objetoCurp.confirmarSelfie()
        
    
        
    
        
