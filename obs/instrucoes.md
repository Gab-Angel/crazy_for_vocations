# Workflow Git — Projeto Compartilhado

## Estrutura das Branches

Cada integrante trabalha em sua própria branch.

Exemplo:

- `main` → versão estável do projeto
- `angel` → branch do Gabriel
- `jorge` → branch do Jorge

---

# Workflow Diário

## 1. Entrar no projeto

```bash
cd crazy_for_vocations
```

## 2. Ir para sua branch

**Gabriel**
```bash
git checkout angel
```

**Jorge**
```bash
git checkout jorge
```

## 3. Atualizar sua branch antes de começar

**Gabriel**
```bash
git pull origin angel
```

**Jorge**
```bash
git pull origin jorge
```

## 4. Programar normalmente

Editar arquivos, criar funcionalidades, corrigir bugs etc.

## 5. Verificar alterações

```bash
git status
```

## 6. Adicionar arquivos

```bash
git add .
```

## 7. Criar commit

**Gabriel**
```bash
git commit -m "feat: adiciona sistema de embeddings"
```

**Jorge**
```bash
git commit -m "feat: adiciona menu inicial"
```

## 8. Enviar alterações para o GitHub

```bash
git push
```

---

## ⚠️ Regra Importante

**NÃO desenvolver diretamente na `main`**

Evitar:

```bash
git push origin main
```

Durante o desenvolvimento normal, tudo deve ir para:

- `angel`
- `jorge`

---

# Como Atualizar sua Branch com a Main

Quando a `main` receber novas funcionalidades:

## 1. Ir para a main

```bash
git checkout main
```

## 2. Atualizar a main

```bash
git pull origin main
```

## 3. Voltar para sua branch

**Gabriel**
```bash
git checkout angel
```

**Jorge**
```bash
git checkout jorge
```

## 4. Trazer mudanças da main

**Gabriel**
```bash
git merge main
```

**Jorge**
```bash
git merge main
```

---

# Como Juntar uma Feature na Main

Quando uma funcionalidade estiver pronta:

## 1. Ir para a main

```bash
git checkout main
```

## 2. Atualizar a main

```bash
git pull origin main
```

## 3. Fazer merge da feature

**Gabriel**
```bash
git merge angel
```

**Jorge**
```bash
git merge jorge
```

## 4. Enviar a main atualizada

```bash
git push origin main
```

---

# Resumo Rápido

## Fluxo diário

```bash
git checkout minha-branch
git pull origin minha-branch
```

Programa normalmente. Depois:

```bash
git add .
git commit -m "mensagem do commit"
git push
```

---

## Comandos Úteis

**Ver branches**
```bash
git branch
```

**Ver todas as branches**
```bash
git branch -a
```

**Criar nova branch**
```bash
git checkout -b nome-da-branch
```

**Deletar branch local**
```bash
git branch -d nome-da-branch
```

**Forçar deleção da branch**
```bash
git branch -D nome-da-branch
```

**Deletar branch remota**
```bash
git push origin --delete nome-da-branch
```

---

## 🏆 Regra de Ouro

Sempre antes de commitar:

```bash
git status
```